import sqlite3
import os


DB = "/Users/makasimba/PycharmProjects/bot/data/users.db"

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

table = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        address VARCHAR(50) NOT NULL,
        phone_number VARCHAR(50) NOT NULL,
        benefits VARCHAR(120) NOT NULL,
        appstage VARCHAR(100) DEFAULT 'form submitted and under review',
        synopsis VARCHAR(1000) DEFAULT '',
        app_id UUID NOT NULL
    );"""

cursor.execute(table)

cursor.execute("""
    INSERT INTO users (first_name, last_name, address, phone_number, benefits)
    VALUES ('Jon', 'Snow', '1101, Winter Fall, The North', '440211120', 'Income-related Employment and Support Allowance')
""")

cursor.execute("""
    INSERT INTO users (first_name, last_name, address, phone_number, benefits)
    VALUES ('Rhaenyra', 'Tagaryen', '1, Golden Road, Dragon Stone', '440211120', 'Universal Basic Income')
""")

cursor.execute("""
    INSERT INTO users (first_name, last_name, address, phone_number, benefits)
    VALUES ('Daemon', 'Targaryen', '1921, Fire Lane, The Vale', '440211120', 'Working Tax Credit')
""")

cursor.execute("""
    INSERT INTO users (first_name, last_name, address, phone_number, benefits)
    VALUES ('Little', 'Finger', '2b, Flea Bottom, The Vale', '440211120', 'Child benefit where the occupants meet the below income thresholds*')
""")

cursor.execute("""
    SELECT *
    FROM users;
""")

print(cursor.fetchall())

conn.commit()
