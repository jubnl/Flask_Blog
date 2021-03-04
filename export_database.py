from utilities.utilities import get_config
from os import system
config = get_config()
try:
    system(f'mysqldump -u {config["db_user"]} -p {config["db_password"]} {config["db_name"]} > dump.sql')
except Exception as e:
    print("An exception has occured..")
    print(e)