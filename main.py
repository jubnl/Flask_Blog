# import all libs and blueprints
from blueprints.account import account_page
from blueprints.admin_logs import admin_logs_page
from blueprints.admin_posts import admin_posts_page
from blueprints.admin_users import admin_users_page
from blueprints.admin import admin_page
from blueprints.authentification import authentification
from blueprints.error_handler import error_handler
from blueprints.home import home_page
from blueprints.registration import registration
from flask import Flask



app = Flask(__name__)

app.config['SECRET_KEY'] = '81016bdd78c9af84f475360d3f045f33'


app.register_blueprint(account_page)
app.register_blueprint(admin_logs_page)
app.register_blueprint(admin_posts_page)
app.register_blueprint(admin_users_page)
app.register_blueprint(admin_page)
app.register_blueprint(authentification)
app.register_blueprint(error_handler)
app.register_blueprint(home_page)
app.register_blueprint(registration)


if __name__ == '__main__':
    app.run(debug=True)

