from blueprints.utils import is_user_logged_in, is_admin
from flask import (
    Blueprint,
    render_template
)


admin_page = Blueprint('admin_page', __name__, template_folder="templates")


@admin_page.route("/admin", methods=['POST', 'GET'])
@is_user_logged_in
@is_admin
def admin():
    return render_template("admin/admin.html", title="Administration")