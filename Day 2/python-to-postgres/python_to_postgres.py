import psycopg2

hostname = "localhost"
database = "demodb"
username = "postgres"
pwd = "72223142cliffochieng"
port_id = 5432

conn = None
cur = None

# Connecting the database
try:
    conn = psycopg2.connect(
        host=hostname, dbname=database, user=username, password=pwd, port=port_id
    )

    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS employee")

    create_script = """ CREATE TABLE IF NOT EXISTS employee (
                            id      int PRIMARY KEY,
                            name    varchar(40) NOT NULL,
                            salary  int,
                            dept_id varchar(30)
    )
"""

    cur.execute(create_script)

    insert_script = "INSERT INTO employee (id, name, salary, dept_id) VALUES (%s, %s, %s, %s)"

    insert_values = [(1, "Houdini", 50000, "IT"), (2, "Papi", 55000, "FO"), (3, "Chulo", 60000, "PM")]

    for record in insert_values:
        cur.execute(insert_script, record)

    conn.commit()


except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
