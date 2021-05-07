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
from flask import Flask, url_for, redirect



app = Flask(__name__)

# CHANGE THAT KEY TO YOUR OWN KEY !
# you can do that by oppening a python prompt and type :
# >>> import secrets
# >>> secrets.token_hex()
# 'd636881cff3a920fffd007dd5f4222cd140ffc68e3d83223ac84adcd027e19b3'

app.config['SECRET_KEY'] = '179ac44220eba6212e3843824faaa6ff1e45d3c847a51f22204dbc9b2791d40d'


app.register_blueprint(account_page)
app.register_blueprint(admin_logs_page)
app.register_blueprint(admin_posts_page)
app.register_blueprint(admin_users_page)
app.register_blueprint(admin_page)
app.register_blueprint(authentification)
app.register_blueprint(error_handler)
app.register_blueprint(home_page)
app.register_blueprint(registration)

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))

if __name__ == '__main__':
    app.run()

