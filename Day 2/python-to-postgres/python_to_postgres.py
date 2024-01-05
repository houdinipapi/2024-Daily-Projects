import psycopg2
import psycopg2.extras

hostname = "localhost"
database = "demodb"
username = "postgres"
pwd = "yourpassword"
port_id = 5432

conn = None
# cur = None

# Connecting the database
try:
    with psycopg2.connect(
        host=hostname, dbname=database, user=username, password=pwd, port=port_id
    ) as conn:
        with conn.cursor(
            cursor_factory=psycopg2.extras.DictCursor
        ) as cur:  # Reading a large database in dict form
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

            insert_values = [
                (1, "Houdini", 50000, "IT"),
                (2, "Papi", 55000, "FO"),
                (3, "Chulo", 60000, "PM"),
            ]

            for record in insert_values:
                cur.execute(insert_script, record)

            # Updating the tables
            update_script = "UPDATE employee SET salary = salary + (salary * 0.5)"
            cur.execute(update_script)

            # Deleting data from the table
            delete_script = "DELETE FROM employee WHERE name = %s"
            delete_record = ("Chulo",)
            cur.execute(delete_script, delete_record)

            cur.execute("SELECT * FROM EMPLOYEE")
            for record in cur.fetchall():
                print(record["name"], record["salary"])

            # conn.commit()


except Exception as error:
    print(error)
finally:
    # if cur is not None:
    #     cur.close()
    if conn is not None:
        conn.close()
