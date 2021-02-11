from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField, TextAreaField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp, ValidationError
from models.model import Model
from models.filter import Filter
from flask import session
from re import compile
from passlib.hash import sha256_crypt


class RegistrationForm(FlaskForm):

    username = StringField('Nom d\'utilisateur',
        validators=[
            DataRequired(message="Vous devez remplir ce champs."),
            Length(min=2,max=20,
                message="Le nom d'utilisateur doit faire entre 2 et 20 caractères")
        ]
    )
    
    fname = StringField('Prénom',
        validators=[
            DataRequired(message="Vous devez remplir ce champs."),
            Length(min=2,max=100, message="Le nom de famille entré doit faire entre 2 et 100 caractères.")
        ]
    )
    
    lname = StringField('Nom de famille',
        validators=[
            DataRequired(message="Vous devez remplir ce champs."),
            Length(min=2,max=100, message="Le prénom entré doit faire entre 2 et 100 caractères.")
        ]
    )
    
    model = Model("t_genders")
    query = model.query_all_rows(fields=['gender'])
    choices = []
    for i in query:
        choices.append(i['gender'])
    
    gender = SelectField("Genre",
        validators=[
            DataRequired(message="Veuillez séléctionner un genre")
        ],
        choices=choices
    )
    
    model = Model("t_countries")
    filter = Filter(order_by={'name':'ASC'})
    query = model.query_all_rows(fields=['name'])
    choices = []
    for i in query:
        choices.append(i['name'])
    
    
    country = SelectField('Pays',
        validators=[
            DataRequired(message="Veuillez selectionner un pays.")
        ],
        choices=choices
    )

    email = StringField('Email',
        validators=[
            DataRequired(message="Vous devez remplir ce champs."),
            Email(message="Veuillez entrer une adresse mail valide."),
            Length(min=5,max=255, message="L'email doit faire entre 5 et 255 caractères.")
        ]
    )

    confirm_email = StringField('Confirmez votre Email',
        validators=[
            DataRequired(message="Vous devez remplir ce champs."),
            EqualTo('email', message="Les adresses mails doivent correspondre.")
        ]
    )

    password = PasswordField('Mot de passe',
        validators=[
            DataRequired(message="Vous devez remplir ce champs."),
            Regexp("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,50}$",
                message="Le mot de passe doit faire entre 8 et 50 caractères avec au minimum une MAJUSCULE, une minuscule, un chiffre et un caractère spécial.")
        ]
    )

    confirm_password = PasswordField('Confirmez votre mot de passe',
        validators=[
            DataRequired(message="Vous devez remplir ce champs."),
            EqualTo('password', message="Les mots de passes doivent correspondre.")
        ]
    )

    submit = SubmitField('Rejoindre')


class LoginForm(FlaskForm):

    email = StringField('Email',
        validators=[DataRequired(message="Vous devez remplir ce champs."),
            Email()
        ]
    )

    password = PasswordField('Password',
        validators=[DataRequired(message="Vous devez remplir ce champs.")]
    )
    
    remember = BooleanField('Remember Me')

    submit = SubmitField('Sign in')
    
    

class UpdateAccountForm(FlaskForm):
    username = StringField('Nom d\'utilisateur',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    
    fname = StringField('Prénom',
        validators=[
            DataRequired(message="Vous devez remplir ce champs."),
            Length(min=2,max=100, message="Le nom de famille entré doit faire entre 2 et 100 caractères.")
        ]
    )
    
    lname = StringField('Nom de famille',
        validators=[
            DataRequired(message="Vous devez remplir ce champs."),
            Length(min=2,max=100, message="Le prénom entré doit faire entre 2 et 100 caractères.")
        ]
    )
    
    model = Model("t_genders")
    query = model.query_all_rows(fields=['gender'])
    choices = []
    for i in query:
        choices.append(i['gender'])
    
    gender = SelectField("Genre",
        validators=[
            DataRequired(message="Veuillez séléctionner un genre")
        ],
        choices=choices
    )
    
    model = Model("t_countries")
    filter = Filter(order_by={'name':'ASC'})
    query = model.query_all_rows(fields=['name'])
    choices = []
    for i in query:
        choices.append(i['name'])
    
    
    country = SelectField('Pays',
        validators=[
            DataRequired(message="Veuillez selectionner un pays.")
        ],
        choices=choices
    )
    
    new_password = PasswordField('Nouveau mot de passe',
    
    )

    confirm_new_password = PasswordField('Confirmez votre nouveau mot de passe',
        validators=[
            EqualTo('new_password', message="Les mots de passes doivent correspondre.")
        ]
    )
    
    confirm_old_password = PasswordField('Confirmez votre ancien mot de passe')
    
    
    submit = SubmitField('Update')
    
    def validate_confirm_new_password(self, confirm_new_password):
        if self.new_password.data == "" or confirm_new_password.data == "":
            return
        prog = compile("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,50}$")
        result = prog.fullmatch(confirm_new_password.data)
        if result is None:
            raise ValidationError("Le mot de passe doit faire entre 8 et 50 caractères avec au minimum une MAJUSCULE, une minuscule, un chiffre et un caractère spécial.")


    def validate_username(self, username):
        if username.data != session["user_username"]:
            filter=Filter(where=f"`username` = '{username.data}'")
            user = Model("t_users").query_one_row(filter=filter)
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')
    
    def validate_confirm_old_password(self, confirm_old_password):
        password = Model("t_users").query_one_row(filter=Filter(where=f"`username` = '{session['user_username']}'"), fields=['password'])['password']
        if self.new_password.data == "" or self.confirm_new_password.data == "" or confirm_old_password.data == "":
            return
        if confirm_old_password.data == self.confirm_new_password.data:
            raise ValidationError("Votre ancien mot de passe et votre nouveau mot de passe doivent être différents !")
        if not sha256_crypt.verify(confirm_old_password.data, password):
            raise ValidationError("L'ancien mot de passe n'est pas correct.")

    def validate_email(self, email):
        if email.data != session["user_email"]:
            filter=Filter(where=f"`email` = '{email.data}'")
            user = Model("t_users").query_one_row(filter=filter)
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')
            



class AdminUserForm(FlaskForm):
    
    model = Model("t_permissions")
    query = model.query_all_rows()
    
    choices =[]
    for i in query:
        choices.append(i['permission'])
    
    permission = SelectField("Permission", choices=choices)
    
    username = StringField('Nom d\'utilisateur',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    
    model = Model("t_genders")
    query = model.query_all_rows(fields=['gender'])
    choices = []
    for i in query:
        choices.append(i['gender'])
    
    gender = SelectField("Genre",
        validators=[
            DataRequired(message="Veuillez séléctionner un genre")
        ],
        choices=choices
    )
    
    model = Model("t_countries")
    filter = Filter(order_by={'name':'ASC'})
    query = model.query_all_rows(fields=['name'])
    choices = []
    for i in query:
        choices.append(i['name'])
    
    
    country = SelectField('Pays',
        validators=[
            DataRequired(message="Veuillez selectionner un pays.")
        ],
        choices=choices
    )
    submit = SubmitField('Update')
    
    

class LogsForm(FlaskForm):
    
    id = IntegerField("ID")
    
    user_id = StringField("Username")
    
    log_type_id = StringField("Log type")
    
    sql_executed = TextAreaField("SQL executed")
    
    value_before = StringField("Value before")
    
    value_after = StringField("Value after")
    
    success = StringField("Success")
    
    log_date = StringField("Log date")
    
    error_message = StringField("Error message")
    
    deleted_data = TextAreaField("Deleted datas")