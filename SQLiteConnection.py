import sqlite3

def createTable() -> None:
    # create/connect to db
    conn = sqlite3.connect("customer.db")

    # create cursor
    c = conn.cursor()

    # create a table
    c.execute("""CREATE TABLE customers (
            first_name TEXT,
            last_name TEXT,
            email TEXT
        )""")
    # DATATYPES in SQLite
    # NULL
    # INTEHER
    # REAL
    # TEXT
    # BLOB mp3 mp4 video pictures....

    # Commit our command
    conn.commit()

    #Close our connection
    conn.close()

def insertDatainDB() -> None:
    # create/connect to db
    conn = sqlite3.connect("customer.db")

    # create cursor
    c = conn.cursor()

    # create a table
    c.execute("INSERT INTO customers VALUES ('John','Elder','Johny@codemy.com')")

    # Commit our command
    conn.commit()

    #Close our connection
    conn.close()

def insertManyDatainDB() -> None:
    # create/connect to db
    conn = sqlite3.connect("customer.db")

    # create cursor
    c = conn.cursor()

    many_customers = [
                        ('Flemming','Mikkel','ditto@hotmail.com'),
                        ('Manuel','Ole','fitto@hotmail.com'),
                        ('Mikkel','Bob','gitto@hotmail.com')
                    ]

    # create a table
    c.executemany("INSERT INTO customers VALUES (?,?,?)",many_customers)

    # Commit our command
    conn.commit()

    #Close our connection
    conn.close()

def QueryTheDataBase() -> None:
    # create/connect to db
    conn = sqlite3.connect("customer.db")

    # create cursor
    c = conn.cursor()

    # Query the Database
    c.execute("SELECT * FROM customers")
    #c.fetchone()
    #c.fetchmany(3)
    #c.fetchall()
    print(c.fetchall())

    conn.commit()

    c.close()

def QuerySearchTheDataBase() -> None:
    # create/connect to db
    conn = sqlite3.connect("customer.db")

    # create cursor
    c = conn.cursor()

    # Query the Database
    c.execute("SELECT * FROM customers")

    items = c.fetchall()

    for item in items:
        print(item[0])

    conn.commit()

    c.close()

def QueryPrimaryKeyDataBase() -> None:
    # create/connect to db
    conn = sqlite3.connect("customer.db")

    # create cursor
    c = conn.cursor()

    # Query the Database with Primary key
    # SQLite automatically add rowID's for each record "set of data"
    c.execute("SELECT rowid,* FROM customers")

    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()

    c.close()

def SearchSpecificThinginTheDataBase() -> None:
    # create/connect to db
    conn = sqlite3.connect("customer.db")

    # create cursor
    c = conn.cursor()

    # Query the Database with Primary key
    # SQLite automatically add rowID's for each record "set of data"
    c.execute("SELECT * FROM customers WHERE last_name = 'Mikkel'")

    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()

    c.close()

def UpdateRecordsInTheDataBase() -> None:
    # create/connect to db
    conn = sqlite3.connect("customer.db")

    # create cursor
    c = conn.cursor()

    # Update Record
    c.execute("""UPDATE customers SET first_name = 'Bob' 
                 WHERE rowid = 1    
    """)

    conn.commit()

    c.execute("SELECT rowid,* FROM customers")

    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()

    c.close()

def DeleteRecordsInTheDataBase() -> None:
    # create/connect to db
    conn = sqlite3.connect("customer.db")

    # create cursor
    c = conn.cursor()

    # Query the Database with Primary key
    # SQLite automatically add rowID's for each record "set of data"
    c.execute("DELETE FROM customers WHERE rowid = 6")

    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()

    c.close()