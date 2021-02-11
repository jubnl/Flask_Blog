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

                query = model.update_rows(fields_values={'files':picture_file}, filter=filter)
                if query is not True:
                    flash(f'An error occured while updating your account.. {query} picture', 'danger')
                    return redirect(url_for('account_page.account'))

            # change username
            if form.username.data != session['user_username']:
                session["user_username"] = form.username.data
                query = model.update_rows(fields_values={'username':form.username.data}, filter=filter)
                
                if query is not True:
                    flash(f'An error occured while updating your account.. {query} username', 'danger')
                    return redirect(url_for('account_page.account'))
            
            # change email
            if form.email.data != session['user_email']:
                session["user_email"] = form.email.data
                query = model.update_rows(fields_values={'email':form.email.data}, filter=filter)
                
                if query is not True:
                    flash(f'An error occured while updating your account.. {query} email', 'danger')
                    return redirect(url_for('account_page.account'))
            
            # change fname
            if form.fname.data != session['fname']:
                session['fname'] = form.fname.data
                query = model.update_rows(fields_values={'first_name':form.fname.data}, filter=filter)

                if query is not True:
                    flash(f'An error occured while updating your account.. {query} fname', 'danger')
                    return redirect(url_for('account_page.account'))
            
            # change lname
            if form.lname.data != session['lname']:
                session['lname'] = form.lname.data
                query = model.update_rows(fields_values={'last_name':form.lname.data}, filter=filter)

                if query is not True:
                    flash(f'An error occured while updating your account.. {query} lname', 'danger')
                    return redirect(url_for('account_page.account'))
            
            # change password
            if form.confirm_old_password.data != "" and form.confirm_new_password.data != "" and form.new_password.data != "":
                phash = sha256_crypt.hash(str(form.confirm_new_password.data))
                
                query = model.update_rows(fields_values={'password':phash}, filter=filter)
                

                if query is not True:
                    flash(f'An error occured while updating your account.. {query} password', 'danger')
                    return redirect(url_for('account_page.account'))
            
            
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
                query = model.update_rows(fields_values={'country':country}, filter=filter)

                if query is not True:
                    flash(f'An error occured while updating your account.. {query} : country block', 'danger')
                    return redirect(url_for('account_page.account'))
            
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
                query = model.update_rows(fields_values={'gender':gender}, filter=filter)

                if query is not True:
                    flash(f'An error occured while updating your account.. {query} gender', 'danger')
                    return redirect(url_for('account_page.account'))
            
            
                
            
            
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

