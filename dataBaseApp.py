import sqlite3

def show_all() -> None:
    ''' Query The DB and Return All Recods'''
    conn, c = connect_to_dataBase()

    # Query The Database
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()
    for item in items:
        print(item)

    commit_and_close_database_connection(conn)

def add_one_record_to_table(first_name, last_name, birthday)-> None:
    ''' add one new Record to table'''
    conn, c = connect_to_dataBase()

    # Query The Database
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first_name, last_name, birthday))

    commit_and_close_database_connection(conn)

def add_many_records_to_table(list)-> None:
    ''' add many new Records to table'''
    conn, c = connect_to_dataBase()

    # Query The Database
    c.execute("INSERT INTO customers VALUES (?,?,?)", (list))

    commit_and_close_database_connection(conn)

def delete_one_record_from_table(id) -> None:
    ''' delete one Record from table (id = string)'''
    conn, c = connect_to_dataBase()

    # Query The Database
    c.execute("DELETE from customers WHERE rowid = (?)", id)

    commit_and_close_database_connection(conn)

def connect_to_dataBase():
    ''' connect to database and create cursor'''
    # Connect to database
    conn = sqlite3.connect("customer.db")
    # Create a cursor
    c = conn.cursor()

    return conn, c

def commit_and_close_database_connection(conn) -> None:
    ''' commit and close connection to database'''
     # Commit our command
    conn.commit()

    # Close our connection
    conn.close()