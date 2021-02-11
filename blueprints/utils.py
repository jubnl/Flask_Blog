from os.path import splitext, join
from secrets import token_hex
from PIL import Image
from functools import wraps
from pathlib import Path
from flask import (
    url_for, flash,
    redirect,
    session,
    abort
)

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
            abort(404)
    return wrap



def save_picture(form_picture):
    random_hex = token_hex(8)
    _, f_ext = splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = (Path.cwd() / f"static/profile_pics/{picture_fn}").resolve()

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn