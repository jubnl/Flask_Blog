from forms import RegistrationForm
from passlib.hash import sha256_crypt
from models.model import Model
from models.filter import Filter
from flask import (
    Blueprint,
    render_template,
    url_for, flash,
    redirect,
    request,
)


registration = Blueprint('registration', __name__, template_folder="templates")


# register page
@registration.route('/register', methods=['GET', 'POST'])
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
            return render_template('register/register.html', title="S'inscrire", form=form)
        
        # get gender's id
        model = Model("t_genders")
        filter = Filter(where=f"`gender` = '{form.gender.data}'")
        gender_id = model.query_one_row(filter = filter)['id']
        if not isinstance(gender_id, int):
            flash("Something went wrong..")
            return render_template('register/register.html', title="S'inscrire", form=form)
        
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
        sql_query, query = model.insert_into_single_record(fields_values=insert, return_sql_query=True)
        
        # if the query was not successful
        if query is not True:
            
            sql_query = sql_query.replace('"', r'\"')
            sql_query = sql_query.replace("'", r"\'")
            query_str = str(query)
            query_str = query_str.replace('"', r'\"')
            query_str = query_str.replace("'", r"\'")
            
            insert_log = {
                'log_type_id'   : Model("t_log_types").query_one_row(filter=Filter(where="`log_type` = 'add_user'"), fields= ['id'])['id'],
                'sql_executed'  : sql_query,
                'success'       : 0,
                'error_message' : query_str
            }
            
            log = Model("t_logs")
            res = log.insert_into_single_record(fields_values=insert_log)
            # error message if duplicate entry
            if query.args[0] == 1062:
                if "username" in query.args[1]:
                    flash(f'Le nom d\'utilisateur {form.username.data} existe déjà ! Veuillez en choisir un autre','danger')
                if "email" in query.args[1]:
                    flash(f'L\'email {form.email.data} existe déjà ! Veuillez en choisir un autre','danger')
            
            # basic error message
            else:
                flash(f'Une erreur est survenue lors de la création du compte de {form.username.data} ! Veuillez contacter le webmaster !','danger')
            return render_template('register/register.html', title="S'inscrire", form=form)
        
        # account created correctly
        else:
            flash(f'Compte crée pour {form.username.data} !','success')
            return redirect(url_for('home_page.home'))
        
    return render_template('register/register.html', title="S'inscrire", form=form)