from blueprints.utils import is_user_logged_in
from flask import (
    Blueprint,
    render_template
)


home_page = Blueprint('home_page', __name__, template_folder="templates")

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


# home page
@home_page.route('/')
def home():
    return render_template('home/home.html',posts=posts, title="Home", sidebar=True)


# about the blog page
@home_page.route('/about/')
@is_user_logged_in
def about():
    return render_template('home/about.html',title="About", sidebar=True)