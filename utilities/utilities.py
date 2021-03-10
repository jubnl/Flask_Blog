# made by https://github.com/jubnl

import json
from pathlib import Path
import pymysql.cursors


def get_config():
    """retourne la config, ne prends pas de paramètres"""

    # set le path pour la config
    mod_path = Path(__file__).parent
    relative_path = '../config/db_config.json'
    config_bot_json = (mod_path / relative_path).resolve()

    # ouvre le fichier et le met dans une var (referme le fichier tout seul)
    with open(config_bot_json,'r') as js_config:
        config = json.load(js_config)

    #retourne la config
    return config


def conn_db():
    """Connexion à la db, ne prends pas de paramètres"""

    # obtient la config
    config = get_config()

    # set les paramètres de configuration pour la connexion à la db
    conn=pymysql.connect(
        host=config["db_host"],
        port=config["db_port"],
        user=config["db_user"],
        password=config["db_password"],
        db=config["db_name"],
        charset = "utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )
    # retourne les paramètres de connexion à la db
    return conn


def parse_sql(filename:str):
    data = open(filename, 'r').readlines()
    stmts = []
    DELIMITER = ';'
    stmt = ''

    for lineno, line in enumerate(data):
        if not line.strip():
            continue

        if line.startswith('--'):
            continue

        if 'DELIMITER' in line:
            DELIMITER = line.split()[1]
            continue

        if (DELIMITER not in line):
            stmt += line.replace(DELIMITER, ';')
            continue

        if stmt:
            stmt += line
            stmts.append(stmt.strip())
            stmt = ''
        else:
            stmts.append(line.strip())
    return stmts

