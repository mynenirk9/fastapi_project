import sqlite3


def create_table():
    conn_obj = sqlite3.connect("sql_app.db")
    cur = conn_obj.cursor()

    cur.execute("""
        CREATE TABLE employee (
            id integer primary key AUTOINCREMENT,
            emp_id integer,
            emp_name char(50)
        )
    """)

    print("table created")
    conn_obj.close()


if __name__ == "__main__":
    create_table()
