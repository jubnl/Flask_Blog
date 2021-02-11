from os.path import splitext, join
from secrets import token_hex
from functools import wraps
from forms import RegistrationForm, LoginForm, UpdateAccountForm, AdminUserForm
from passlib.hash import sha256_crypt
from models.model import Model
from models.filter import Filter
from PIL import Image
from flask import (
    Flask,
    render_template,
    url_for, flash,
    redirect,
    request,
    session,
    abort
)


app = Flask(__name__)

app.config['SECRET_KEY'] = '81016bdd78c9af84f475360d3f045f33'



posts = [
    {
        'author' : 'asdf',
        'title' : 'asdf',
        'date_posted' : '2018',
        'content':'asdf'
    },
    {
        'author' : 'asdf',
        'title' : 'sadf',
        'date_posted' : '2019',
        'content':'asdf'
    }
]

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="404"), 404

# decorator that check if a user is logged in
def is_user_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'user_logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Veuillez vous connecter pour accéder à cette ressource.', 'danger')
            return redirect(url_for('login'))
    return wrap

# decorator that check if a user is admin
def is_admin(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if session['perms'] == 3:
            return f(*args, **kwargs)
        else:
            flash('Vous devez être Administrateur pour accéder à cette ressource.', 'danger')
            return redirect(url_for('login'))
    return wrap


# home page
@app.route('/')
def home():
    return render_template('home.html',posts=posts, title="Home")


# logout page (just clear session)
@app.route("/logout")
def logout():
    session.clear()
    flash('Vous êtes maintenant déconnecté', 'success')
    return redirect(url_for('home'))


# about the blog page
@app.route('/about/')
@is_user_logged_in
def about():
    return render_template('about.html',title="About")


# register page
@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    
    # if the form is valid, insert data in the database
    if request.method == 'POST' and form.validate_on_submit():
        
        # get country's id
        model = Model("t_countries")
        filter = Filter(where=f"`name` = '{form.country.data}'")
        country_id = model.query_one_row(filter = filter)['id']
        if not isinstance(country_id, int):
            flash("Something went wrong..")
            return render_template('register.html', title="S'inscrire", form=form)
        
        # get gender's id
        model = Model("t_genders")
        filter = Filter(where=f"`gender` = '{form.gender.data}'")
        gender_id = model.query_one_row(filter = filter)['id']
        if not isinstance(gender_id, int):
            flash("Something went wrong..")
            return render_template('register.html', title="S'inscrire", form=form)
        
        # dict insert datas
        insert = {
            'permission'                : 1,
            'first_name'                : form.fname.data,
            'last_name'                 : form.lname.data,
            'email'                     : form.email.data,
            'country'                   : country_id,
            'username'                  : form.username.data,
            'password'                  : sha256_crypt.hash(str(form.password.data)),
            'reset_password_permission' : "no_reset",
            'files'                     : "admin.png",
            'gender'                    : gender_id,
            'reset_password_random'     : "Default_value"
        }
        
        # insert datas
        model = Model("t_users")
        query = model.insert_into_single_record(insert)
        
        # if the query was not successful
        if query is not True:
            print(query)
            
            # error message if duplicate entry
            if query.args[0] == 1062:
                if "username" in query.args[1]:
                    flash(f'Le nom d\'utilisateur {form.username.data} existe déjà ! Veuillez en choisir un autre','danger')
                if "email" in query.args[1]:
                    flash(f'L\'email {form.email.data} existe déjà ! Veuillez en choisir un autre','danger')
            
            # basic error message
            else:
                flash(f'Une erreur est survenue lors de la création du compte de {form.username.data} ! Veuillez contacter le webmaster !','danger')
            return render_template('register.html', title="S'inscrire", form=form)
        
        # account created correctly
        else:
            flash(f'Compte crée pour {form.username.data} !','success')
            return redirect(url_for('home'))
        
    return render_template('register.html', title="S'inscrire", form=form)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    # if the user is already logged in, redirect to home()
    if "user_logged_in" in session.keys():
        return redirect(url_for("home"))
    
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
                return redirect(next_page) if next_page else redirect(url_for('home'))
            
            # error message if the password isn't right
            else:
                flash('Le mot de passe est incorrect', 'danger')
                return render_template('login.html', title="Login", form=form)
        
        # error message if the email isnt in the database
        else:
            flash('Le compte est introuvable !', 'danger')
            return render_template('login.html', title="Login", form=form)
    return render_template('login.html', title="Login", form=form)


def save_picture(form_picture):
    random_hex = token_hex(8)
    _, f_ext = splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
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
                    return redirect(url_for('account'))

            # change username
            if form.username.data != session['user_username']:
                session["user_username"] = form.username.data
                query = model.update_rows(fields_values={'username':form.username.data}, filter=filter)
                
                if query is not True:
                    flash(f'An error occured while updating your account.. {query} username', 'danger')
                    return redirect(url_for('account'))
            
            # change email
            if form.email.data != session['user_email']:
                session["user_email"] = form.email.data
                query = model.update_rows(fields_values={'email':form.email.data}, filter=filter)
                
                if query is not True:
                    flash(f'An error occured while updating your account.. {query} email', 'danger')
                    return redirect(url_for('account'))
            
            # change fname
            if form.fname.data != session['fname']:
                session['fname'] = form.fname.data
                query = model.update_rows(fields_values={'first_name':form.fname.data}, filter=filter)

                if query is not True:
                    flash(f'An error occured while updating your account.. {query} fname', 'danger')
                    return redirect(url_for('account'))
            
            # change lname
            if form.lname.data != session['lname']:
                session['lname'] = form.lname.data
                query = model.update_rows(fields_values={'last_name':form.lname.data}, filter=filter)

                if query is not True:
                    flash(f'An error occured while updating your account.. {query} lname', 'danger')
                    return redirect(url_for('account'))
            
            # change password
            if form.confirm_old_password.data != "" and form.confirm_new_password.data != "" and form.new_password.data != "":
                phash = sha256_crypt.hash(str(form.confirm_new_password.data))
                
                query = model.update_rows(fields_values={'password':phash}, filter=filter)
                

                if query is not True:
                    flash(f'An error occured while updating your account.. {query} password', 'danger')
                    return redirect(url_for('account'))
            
            
            # query country id
            model = Model("t_countries")
            filter = Filter(where=f"`name` = '{form.country.data}'")
            country = model.query_one_row(filter=filter)['id']
            if not isinstance(country, int):
                flash(f'An error occured while updating your account.. {country} ss', 'danger')
                return redirect(url_for('account'))
        
            # change country
            if country != session['country']:
                model = Model("t_users")
                filter = Filter(where=f"`id` = {query_user['id']}") 
                session['country'] = country
                query = model.update_rows(fields_values={'country':country}, filter=filter)

                if query is not True:
                    flash(f'An error occured while updating your account.. {query} : country block', 'danger')
                    return redirect(url_for('account'))
            
            # query gender id
            model = Model("t_genders")
            filter = Filter(where=f"`gender` = '{form.gender.data}'")
            gender = model.query_one_row(filter=filter)['id']
            if not isinstance(gender, int):
                flash(f'An error occured while updating your account.. {gender} aa', 'danger')
                return redirect(url_for('account'))
            
            # changer gender
            if gender != session['gender']:
                model = Model("t_users")
                filter = Filter(where=f"`id` = {query_user['id']}") 
                session['gender'] = gender
                query = model.update_rows(fields_values={'gender':gender}, filter=filter)

                if query is not True:
                    flash(f'An error occured while updating your account.. {query} gender', 'danger')
                    return redirect(url_for('account'))
            
            
                
            
            
            flash('Your account has been updated!', 'success')
            return redirect(url_for('account'))
        
        else:
            flash(f'An error occured while updating your account.. {query_user} asdfasdf', 'danger')
            return redirect(url_for('account'))
        
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
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)



@app.route("/admin", methods=['POST', 'GET'])
@is_user_logged_in
@is_admin
def admin():
    return render_template("admin/admin.html", title="Administration")


@app.route("/admin/users", methods=['POST', 'GET'])
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


@app.route("/admin/user/<string:username>", methods=['POST', 'GET'])
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


@app.route("/admin/delete_user/<string:username>", methods=['POST', 'GET'])
@is_user_logged_in
@is_admin
def admin_delete_user(username):
    return render_template("admin/delete_user.html", title="Supression d'un utilisateur")


if __name__ == '__main__':
    app.run(debug=True)
