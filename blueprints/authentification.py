from forms import LoginForm
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


authentification = Blueprint('authentification', __name__, template_folder="templates")



@authentification.route('/login', methods=['GET', 'POST'])
def login():
    # if the user is already logged in, redirect to home()
    if "user_logged_in" in session.keys():
        return redirect(url_for("home_page.home"))
    
    form = LoginForm()
    
    if request.method == 'POST' and form.validate_on_submit():
        
        # verify that the user exists
        email = form.email.data
        password = form.password.data
        model = Model("t_users")
        filter = Filter(where=f"`email` = '{email}'")
        query = model.query_one_row(filter=filter)
        
        # if the user exists
        if query is not None:
            db_password = query['password']
            
            # verify that its the right passowrd
            if sha256_crypt.verify(password, db_password):
                
                # set session cookies
                session['user_logged_in'] = True
                session["user_email"] = query['email']
                session["user_username"] = query['username']
                session['files'] = query['files']
                session['fname'] = query['first_name']
                session['lname'] = query['last_name']
                session['gender'] = query['gender']
                session['country'] = query['country']
                session['perms'] = query['permission']


                # if remember me check box is checked, set session to permanent
                if form.remember.data is True:
                    session.permanent = True
                else:
                    session.permanent = False
                
                
                # flash message + redirect to the right page
                flash('Vous êtes maintenant connecté', 'success')
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('home_page.home'))
            
            # error message if the password isn't right
            else:
                flash('Le mot de passe est incorrect', 'danger')
                return render_template('authentification/login.html', title="Login", form=form)
        
        # error message if the email isnt in the database
        else:
            flash('Le compte est introuvable !', 'danger')
            return render_template('authentification/login.html', title="Login", form=form)
    return render_template('authentification/login.html', title="Login", form=form)


# logout page (just clear session)
@authentification.route("/logout")
def logout():
    session.clear()
    flash('Vous êtes maintenant déconnecté', 'success')
    return redirect(url_for('home_page.home'))