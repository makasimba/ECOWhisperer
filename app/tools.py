import datetime
import sqlite3


DB = "/Users/makasimba/PycharmProjects/bot/data/users.db"


def get_date():
    """Returns the current date as a formatted string"""
    return datetime.datetime.now().strftime("%A %d, %B %Y")


def add_user_to_db(user):
    conn = sqlite3.connect(DB)

    with conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (first_name, last_name, address, phone_number, benefits)
            VALUES (?, ?, ?, ?, ?)""", user)


def get_user_information_from_db(app_id):
    conn = sqlite3.connect(DB)

    with conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM users
            WHERE app_id=?""", app_id)
