from blueprints.utils import is_user_logged_in, is_admin
from forms import AdminUserForm
from models.model import Model
from models.filter import Filter
from flask import (
    Blueprint,
    render_template,
    url_for,
    abort
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
    
    return render_template("admin/user.html", title="Administration",form=form, image_file=image_file)


@admin_users_page.route("/admin/delete_user/<string:username>", methods=['POST', 'GET'])
@is_user_logged_in
@is_admin
def admin_delete_user(username):
    model = Model("t_users")
    filter = Filter(where=f"`username` = '{username}'")
    user = model.query_one_row(filter = filter)
    if user is None:
        abort(404)
    return render_template("admin/delete_user.html", title="Supression d'un utilisateur")