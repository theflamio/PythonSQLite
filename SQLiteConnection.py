import sqlite3

# create/connect to db
conn = sqlite3.connect("customer.db")

# create cursor
c = conn.cursor()

# create a table
c.execute("""CREATE TABLE customers (
        first_name DATATYPE,
        last_name DATATYPE,
        email DATATYPE
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