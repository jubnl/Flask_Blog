from flask import (
    Blueprint,
    render_template
)


error_handler = Blueprint('error_handler', __name__, template_folder="templates")


@error_handler.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html', title="404", sidebar=True), 404