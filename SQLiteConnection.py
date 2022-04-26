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