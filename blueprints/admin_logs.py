from blueprints.utils import is_user_logged_in, is_admin
from forms import LogsForm
from models.model import Model
from models.filter import Filter
from datetime import timedelta
from flask import (
    Blueprint,
    render_template,
    abort
)


admin_logs_page = Blueprint("admin_logs_page", __name__, template_folder="templates")




@admin_logs_page.route("/admin/logs", methods=['POST', 'GET'])
@is_user_logged_in
@is_admin
def logs():
    logs = Model("t_logs").query_all_rows(filter=Filter(order_by={'id':'DESC'}))
    for log in logs:
        
        filter = Filter(where=f"`id` = {log['user_id']}")
        username = Model("t_users").query_one_row(filter=filter, fields=['username'])
        if not isinstance(username, dict):
            log['user_id'] = "Flask"
        else:
            log['user_id'] = username['username']
        
        filter = Filter(where=f"`id` = {log['log_type_id']}")
        log_type = Model("t_log_types").query_one_row(filter=filter, fields=['designation'])['designation']
        log['log_type_id'] = log_type
        
        log['log_date'] = (log['log_date'] + timedelta(hours=1)).strftime("%d/%b/%Y - %H:%M:%S")
        
        if log['success'] == 1: log['success'] = True
        else: log['success'] = False
        
    return render_template("admin/logs.html", title="Logs", logs=logs)


@admin_logs_page.route("/admin/log/<int:id>", methods=['POST', 'GET'])
@is_user_logged_in
@is_admin
def log(id):
    model = Model("t_logs")
    filter = Filter(where=f"`id` = {id}")
    log = model.query_one_row(filter = filter)
    if log is None:
        abort(404)
    
    form = LogsForm()
    form.id.data = log['id']
    username = Model("t_users").query_one_row(filter=Filter(where=f"`id` = {log['user_id']}"), fields=['username'])
    if not isinstance(username, dict):
        form.user_id.data = "Flask"
    else:
        form.user_id.data = username['username']
    form.log_type_id.data = Model("t_log_types").query_one_row(filter=Filter(where=f"`id` = {log['log_type_id']}"), fields=['designation'])['designation']
    form.sql_executed.data = log['sql_executed']
    form.value_before.data = log['value_before']
    form.value_after.data = log['value_after']
    if log['success'] == 1: log['success'] = True
    else: log['success'] = False
    form.error_message.data = log['error_message']
    form.deleted_data.data = log['deleted_data']
    form.success.data = log['success']
    form.log_date.data = (log['log_date'] + timedelta(hours=1)).strftime("%d %B %Y - %H:%M:%S")
    return render_template("admin/log.html", title="Log detail", log=log, form=form)