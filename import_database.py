from utilities.utilities import parse_sql, conn_db

stmts = parse_sql("databaseStructure+dataDump.sql")
conn = conn_db()

with conn.cursor() as cursor:
    for stmt in stmts:
        cursor.execute(stmt)
    conn.commit()
