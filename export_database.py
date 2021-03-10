from utilities.utilities import get_config
from os import system
config = get_config()
try:
    system(f'mysqldump --add-drop-database --complete-insert --databases --net_buffer_length=16384 -u {config["db_user"]} -p {config["db_name"]} -r dump.sql')
except Exception as e:
    print("An exception has occured..")
    print(e)
