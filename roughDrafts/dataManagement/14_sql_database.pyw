import sqlite3
from sqlite3 import Error

def setup_sql_db(db_file):
    
    Set up an SQL database connection using SQLite3.

    db_file: Path to the SQLite3 database file.
    return Connection object or None.
    
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"SQLite version: {sqlite3.version}\nConnected to {db_file}")
    except Error as e:
        print(e)
    return conn

def test_sql_db(conn):
    
    Test the SQL database connection by creating a sample table and inserting a record.

    conn: Connection object.
    return None
    
    if conn is None:
        print("No connection established!")
        return

    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)''')
        cursor.execute("INSERT INTO users (name) VALUES ('John Doe')")
        conn.commit()
        print("Table created and sample record inserted.")
    except Error as e:
        print(e)

    # Close the connection
    conn.close()

# Example usage
# db_file = 'path/to/your/database.db'
# conn = setup_sql_db(db_file)
# test_sql_db(conn)
