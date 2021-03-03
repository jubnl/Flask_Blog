from flask.helpers import flash
from blueprints.utils import is_user_logged_in, is_admin
from forms import AdminUserForm
from models.model import Model
from models.filter import Filter
from flask import (
    Blueprint,
    render_template,
    url_for,
    abort,
    redirect,
    session
)


admin_users_page = Blueprint("admin_user_page", __name__, template_folder="templates")


@admin_users_page.route("/admin/users", methods=['POST', 'GET'])
@is_user_logged_in
@is_admin
def admin_users():
    model = Model("t_users")
    users = model.query_all_rows(fields=['id', 'permission', 'username', 'email'])
    
    model = Model("t_permissions")
    permissions = model.query_all_rows()
    for user in users:
        for permission in permissions:
            if user['permission'] == permission['id']:
                user['permission'] = permission['permission']
            
    return render_template("admin/users.html", title="Admin - Utilisateurs",users=users)


@admin_users_page.route("/admin/user/<string:username>", methods=['POST', 'GET'])
@is_user_logged_in
@is_admin
def admin_edit_user(username):
    model = Model("t_users")
    filter = Filter(where=f"`username` = '{username}'")
    user = model.query_one_row(filter = filter)
    if user is None:
        abort(404)
    
    model = Model("t_permissions")
    filter = Filter(where=f"`id` = {user['permission']}")
    perm = model.query_one_row(filter=filter)['permission']
    
    model = Model("t_countries")
    filter = Filter(where=f"`id` = {user['country']}")
    country = model.query_one_row(filter = filter)['name']
        
    model = Model("t_genders")
    filter = Filter(where=f"`id` = {user['gender']}")
    gender = model.query_one_row(filter = filter)['gender']
    
    
    form = AdminUserForm()
    
    form.permission.data = perm
    form.username.data = user['username']
    form.email.data = user["email"]
    form.country.data = country
    form.gender.data = gender
    
    image_file = url_for('static', filename='profile_pics/' + user["files"])
    
    if form.validate_on_submit():
        
        model = Model("t_users")
        filter = Filter(where=f"`id` = {user['id']}")
        
        if form.permission.data != perm:
            
            sql, query = model.update_rows(fields_values={'permission':form.permission.data}, filter=filter, return_sql_query=True)
            
            sql = str(sql).replace('"', r'\"')
            sql = sql.replace("'", r"\'")
            
            insert_log = {
                'user_id'       : user['id'],
                'log_type_id'   : Model("t_log_types").query_one_row(filter=Filter(where="`log_type` = 'update_user_permission'"), fields= ['id'])['id'],
                'sql_executed'  : sql,
                'value_before'  : perm,
                'value_after'   : form.permission.data,
                'success'       : 1
            }
            
            if query is not True:
                query_str = str(query).replace('"', r'\"')
                query_str = query_str.replace("'", r"\'")
                    
                insert_log['success'] = 0
                insert_log['error_message'] = query_str
                
                flash(f'An error occured while updating your account..', 'danger')
                return redirect(url_for('admin_user_page.user'))
            log = Model("t_logs").insert_into_single_record(fields_values=insert_log)


    
    return render_template("admin/user.html", title="Administration",form=form, image_file=image_file)




@admin_users_page.route("/admin/delete_user/<string:username>", methods=['POST', 'GET'])
@is_user_logged_in
@is_admin
def admin_delete_user(username):
    model = Model("t_users")
    filter = Filter(where=f"`username` = '{username}'")
    user = model.query_one_row(filter = filter, fields=['username'])
    if user is None:
        abort(404)
    return render_template("admin/delete_user.html", title="Supression d'un utilisateur", user=user['username'])



@admin_users_page.route("/admin/confirm_user_delete/<string:username>", methods=['POST', 'GET'])
@is_user_logged_in
@is_admin
def confirm_user_delete(username):
    model = Model("t_users")
    filter = Filter(where=f"`username` = '{username}'")
    user = model.query_one_row(filter=filter)
    if user is None:
        abort(404)
    
    sql, delete = model.delete_row(filter=filter, return_sql_query=True)
    
    sql = str(sql).replace('"', r'\"')
    sql = sql.replace("'", r"\'")
                
    insert_log = {
        'user_id'       : Model("t_users").query_one_row(filter=Filter(where=f"`username` = '{session['user_username']}'"), fields=['id'])['id'],
        'log_type_id'   : Model("t_log_types").query_one_row(filter=Filter(where="`log_type` = 'delete_user'"), fields= ['id'])['id'],
        'sql_executed'  : sql,
        'deleted_data'  : user,
        'success'       : 1
    }

    
    if delete is not True:
        
        query_str = str(delete).replace('"', r'\"')
        query_str = query_str.replace("'", r"\'")
                    
        insert_log['success'] = 0
        insert_log['error_message'] = query_str
        
        flash(f"Une erreur est survenue lors de la suppression du compte de {username}", "danger")
        return redirect(url_for('admin_user_page.admin_delete_user', username = username))
    log = Model("t_logs").insert_into_single_record(fields_values=insert_log)
        
    
    return redirect(url_for('admin_user_page.admin_users'))