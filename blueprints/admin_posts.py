from blueprints.utils import is_user_logged_in, is_admin
from flask import (
    Blueprint,
    render_template
)



admin_posts_page = Blueprint("admin_posts_page", __name__, template_folder="templates")


@admin_posts_page.route("/admin/posts", methods=['POST', 'GET'])
@is_user_logged_in
@is_admin
def admin_posts():
    return render_template("admin/posts.html", title="Logs")