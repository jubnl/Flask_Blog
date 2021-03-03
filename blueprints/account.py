from blueprints.utils import save_picture, is_user_logged_in
from forms import UpdateAccountForm
from passlib.hash import sha256_crypt
from models.model import Model
from models.filter import Filter
from flask import (
    Blueprint,
    render_template,
    url_for, flash,
    redirect,
    request,
    session,
)


account_page = Blueprint('account_page', __name__, template_folder="templates")



@account_page.route("/account", methods=['GET', 'POST'])
@is_user_logged_in
def account():
    
    form = UpdateAccountForm()
    
    if form.validate_on_submit():
        
        # query current user in db
        model = Model("t_users")
        filter = Filter(where=f"`email` = '{session['user_email']}'")
        query_user = model.query_one_row(filter=filter)

        if isinstance(query_user, dict):
            
            # set filter for user id
            filter = Filter(where=f"`id` = {query_user['id']}")
            
            # change picture
            if form.picture.data:
                picture_file = save_picture(form.picture.data)
                session['files'] = picture_file

                sql, query = model.update_rows(fields_values={'files':picture_file}, filter=filter, return_sql_query=True)
                
                sql = str(sql).replace('"', r'\"')
                sql = sql.replace("'", r"\'")
                
                insert_log = {
                    'user_id'       : query_user['id'],
                    'log_type_id'   : Model("t_log_types").query_one_row(filter=Filter(where="`log_type` = 'update_user_files'"), fields= ['id'])['id'],
                    'sql_executed'  : sql,
                    'value_before'  : query_user['files'],
                    'value_after'   : picture_file,
                    'success'       : 1
                }
                
                if query is not True:
                    
                    query_str = str(query).replace('"', r'\"')
                    query_str = query_str.replace("'", r"\'")
                    
                    insert_log['success'] = 0
                    insert_log['error_message'] = query_str
                    
                    flash(f'An error occured while updating your account..', 'danger')
                    return redirect(url_for('account_page.account'))
                
                log = Model("t_logs").insert_into_single_record(fields_values=insert_log)

            # change username
            if form.username.data != session['user_username']:
                session["user_username"] = form.username.data
                sql, query = model.update_rows(fields_values={'username':form.username.data}, filter=filter, return_sql_query=True)
                
                sql = str(sql).replace('"', r'\"')
                sql = sql.replace("'", r"\'")
                
                insert_log = {
                    'user_id'       : query_user['id'],
                    'log_type_id'   : Model("t_log_types").query_one_row(filter=Filter(where="`log_type` = 'update_user_username'"), fields= ['id'])['id'],
                    'sql_executed'  : sql,
                    'value_before'  : query_user['username'],
                    'value_after'   : form.username.data,
                    'success'       : 1
                }
                
                if query is not True:
                    
                    query_str = str(query).replace('"', r'\"')
                    query_str = query_str.replace("'", r"\'")
                    
                    insert_log['success'] = 0
                    insert_log['error_message'] = query_str
                    
                    flash(f'An error occured while updating your account..', 'danger')
                    return redirect(url_for('account_page.account'))
                log = Model("t_logs").insert_into_single_record(fields_values=insert_log)
                
            # change email
            if form.email.data != session['user_email']:
                session["user_email"] = form.email.data
                sql, query = model.update_rows(fields_values={'email':form.email.data}, filter=filter, return_sql_query=True)
                
                
                sql = str(sql).replace('"', r'\"')
                sql = sql.replace("'", r"\'")
                
                insert_log = {
                    'user_id'       : query_user['id'],
                    'log_type_id'   : Model("t_log_types").query_one_row(filter=Filter(where="`log_type` = 'update_user_email'"), fields= ['id'])['id'],
                    'sql_executed'  : sql,
                    'value_before'  : query_user['email'],
                    'value_after'   : form.email.data,
                    'success'       : 1
                }
                
                if query is not True:
                    
                    query_str = str(query).replace('"', r'\"')
                    query_str = query_str.replace("'", r"\'")
                    
                    insert_log['success'] = 0
                    insert_log['error_message'] = query_str
                    
                    flash(f'An error occured while updating your account..', 'danger')
                    return redirect(url_for('account_page.account'))
                log = Model("t_logs").insert_into_single_record(fields_values=insert_log)
                
            # change fname
            if form.fname.data != session['fname']:
                session['fname'] = form.fname.data
                sql, query = model.update_rows(fields_values={'first_name':form.fname.data}, filter=filter, return_sql_query=True)
                
                sql = str(sql).replace('"', r'\"')
                sql = sql.replace("'", r"\'")
                
                insert_log = {
                    'user_id'       : query_user['id'],
                    'log_type_id'   : Model("t_log_types").query_one_row(filter=Filter(where="`log_type` = 'update_user_fname'"), fields= ['id'])['id'],
                    'sql_executed'  : sql,
                    'value_before'  : query_user['first_name'],
                    'value_after'   : form.fname.data,
                    'success'       : 1
                }

                if query is not True:
                    
                    query_str = str(query).replace('"', r'\"')
                    query_str = query_str.replace("'", r"\'")
                    
                    insert_log['success'] = 0
                    insert_log['error_message'] = query_str
                    
                    flash(f'An error occured while updating your account.. {query} fname', 'danger')
                    return redirect(url_for('account_page.account'))
                log = Model("t_logs").insert_into_single_record(fields_values=insert_log)
                
            # change lname
            if form.lname.data != session['lname']:
                session['lname'] = form.lname.data
                sql, query = model.update_rows(fields_values={'last_name':form.lname.data}, filter=filter, return_sql_query=True)
                
                
                sql = str(sql).replace('"', r'\"')
                sql = sql.replace("'", r"\'")
                
                insert_log = {
                    'user_id'       : query_user['id'],
                    'log_type_id'   : Model("t_log_types").query_one_row(filter=Filter(where="`log_type` = 'update_user_lname'"), fields= ['id'])['id'],
                    'sql_executed'  : sql,
                    'value_before'  : query_user['last_name'],
                    'value_after'   : form.lname.data,
                    'success'       : 1
                }

                if query is not True:
                    
                    query_str = str(query).replace('"', r'\"')
                    query_str = query_str.replace("'", r"\'")
                    
                    insert_log['success'] = 0
                    insert_log['error_message'] = query_str
                    
                    flash(f'An error occured while updating your account.. {query} lname', 'danger')
                    return redirect(url_for('account_page.account'))
                log = Model("t_logs").insert_into_single_record(fields_values=insert_log)
                
            # change password
            if form.confirm_old_password.data != "" and form.confirm_new_password.data != "" and form.new_password.data != "":
                phash = sha256_crypt.hash(str(form.confirm_new_password.data))
                
                sql, query = model.update_rows(fields_values={'password':phash}, filter=filter, return_sql_query=True)
                
                sql = str(sql).replace('"', r'\"')
                sql = sql.replace("'", r"\'")
                
                insert_log = {
                    'user_id'       : query_user['id'],
                    'log_type_id'   : Model("t_log_types").query_one_row(filter=Filter(where="`log_type` = 'update_user_password'"), fields= ['id'])['id'],
                    'sql_executed'  : sql,
                    'value_before'  : query_user['password'],
                    'value_after'   : phash,
                    'success'       : 1
                }
                

                if query is not True:
                    
                    query_str = str(query).replace('"', r'\"')
                    query_str = query_str.replace("'", r"\'")
                    
                    insert_log['success'] = 0
                    insert_log['error_message'] = query_str
                    
                    flash(f'An error occured while updating your account..', 'danger')
                    return redirect(url_for('account_page.account'))
                log = Model("t_logs").insert_into_single_record(fields_values=insert_log)
            
            # query country id
            model = Model("t_countries")
            filter = Filter(where=f"`name` = '{form.country.data}'")
            country = model.query_one_row(filter=filter)['id']
            if not isinstance(country, int):
                flash(f'An error occured while updating your account.. {country} ss', 'danger')
                return redirect(url_for('account_page.account'))
        
            # change country
            if country != session['country']:
                model = Model("t_users")
                filter = Filter(where=f"`id` = {query_user['id']}") 
                session['country'] = country
                sql, query = model.update_rows(fields_values={'country':country}, filter=filter, return_sql_query=True)
                
                
                sql = str(sql).replace('"', r'\"')
                sql = sql.replace("'", r"\'")
                
                insert_log = {
                    'user_id'       : query_user['id'],
                    'log_type_id'   : Model("t_log_types").query_one_row(filter=Filter(where="`log_type` = 'update_user_country'"), fields= ['id'])['id'],
                    'sql_executed'  : sql,
                    'value_before'  : query_user['country'],
                    'value_after'   : country,
                    'success'       : 1
                }
                

                if query is not True:
                    
                    query_str = str(query).replace('"', r'\"')
                    query_str = query_str.replace("'", r"\'")
                    
                    insert_log['success'] = 0
                    insert_log['error_message'] = query_str
                    
                    flash(f'An error occured while updating your account..', 'danger')
                    return redirect(url_for('account_page.account'))
                log = Model("t_logs").insert_into_single_record(fields_values=insert_log)
                
            # query gender id
            model = Model("t_genders")
            filter = Filter(where=f"`gender` = '{form.gender.data}'")
            gender = model.query_one_row(filter=filter)['id']
            if not isinstance(gender, int):
                flash(f'An error occured while updating your account.. {gender} aa', 'danger')
                return redirect(url_for('account_page.account'))
            
            # changer gender
            if gender != session['gender']:
                model = Model("t_users")
                filter = Filter(where=f"`id` = {query_user['id']}") 
                session['gender'] = gender
                sql, query = model.update_rows(fields_values={'gender':gender}, filter=filter, return_sql_query=True)
                
                sql = str(sql).replace('"', r'\"')
                sql = sql.replace("'", r"\'")
                
                insert_log = {
                    'user_id'       : query_user['id'],
                    'log_type_id'   : Model("t_log_types").query_one_row(filter=Filter(where="`log_type` = 'update_user_gender'"), fields= ['id'])['id'],
                    'sql_executed'  : sql,
                    'value_before'  : query_user['gender'],
                    'value_after'   : gender,
                    'success'       : 1
                }

                if query is not True:
                    
                    query_str = str(query).replace('"', r'\"')
                    query_str = query_str.replace("'", r"\'")
                    
                    insert_log['success'] = 0
                    insert_log['error_message'] = query_str
                    
                    flash('An error occured while updating your account..', 'danger')
                    return redirect(url_for('account_page.account'))
                log = Model("t_logs").insert_into_single_record(fields_values=insert_log)
            
                
            
            
            flash('Your account has been updated!', 'success')
            return redirect(url_for('account_page.account'))
        
        else:
            flash(f'An error occured while updating your account.. {query_user} asdfasdf', 'danger')
            return redirect(url_for('account_page.account'))
        
    elif request.method == 'GET':
        
        model = Model("t_countries")
        filter = Filter(where=f"`id` = {session['country']}")
        country = model.query_one_row(filter = filter)['name']
        
        model = Model("t_genders")
        filter = Filter(where=f"`id` = {session['gender']}")
        gender = model.query_one_row(filter = filter)['gender']
        
        
        form.username.data = session["user_username"]
        form.email.data = session["user_email"]
        form.fname.data = session['fname']
        form.lname.data = session['lname']
        form.country.data = country
        form.gender.data = gender

    image_file = url_for('static', filename='profile_pics/' + session["files"])
    return render_template('account/account.html', title='Account',
                           image_file=image_file, form=form, sidebar=True)

