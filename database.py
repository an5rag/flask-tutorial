import sqlite3
import os

__author__ = 'Anurag'



def set_up_db(database_name):
    # Setting up SQL Database
    # ------------------------
    # The most common way to force an SQLite database
    # to exist purely in memory is to open the database
    # using the special filename ":memory:".
    os.chdir("C:\\Users\\an5ra\\PycharmProjects\\FlaskTutorial")
    con = sqlite3.connect(database_name,check_same_thread=False)

    return con


def create_table(cur):
    # CREATING TABLE
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Comments (C_id INTEGER PRIMARY KEY AUTOINCREMENT ,user_name text, comment_text TEXT, time_stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL);")


# SAMPLE CODE FOR SHOWING TABLE INFORMATION
# -------------------------------------------
# cur.execute("PRAGMA TABLE_INFO(Business);")
# result = cur.fetchall()
# print(result)

def insert_comment(cur, user_name, comment_text):
    comment_tuple = (user_name, comment_text)
    cur.execute("INSERT INTO Comments (user_name, comment_text) VALUES (?, ?);", comment_tuple)
    return cur.lastrowid


def get_comments(cur):
    cur.execute("SELECT * FROM Comments;")
    result = cur.fetchall()
    return result


def drop_all_tables(cur):
    cur.execute("DROP TABLE Comments")

def delete_all_tables(cur):
    cur.execute("DELETE FROM Comments")

