import sqlite3
import logging


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        logging.warning(e)

    return conn


# will delete title from list, if it exist in db
def update_list(conn, list_of_flats):
    cur = conn.cursor()

    for title in list_of_flats:
        cur.execute("SELECT * FROM flats WHERE title=?", (title,))
        rows = cur.fetchall()

        if(len(rows) != 0):
            list_of_flats.remove(title)

    return list_of_flats


def input_new_titles(conn, list_of_flats):
    cur = conn.cursor()

    for title in list_of_flats:
        cur.execute("INSERT INTO flats (title) VALUES (?)", (title,))
        conn.commit()


db_file = "flats_olx.db"
db_connection = create_connection(db_file)
list1 = ["Димас", "Длинное соощение, которое почему-то пропускается и добавляется несколько раз"]
update_list(db_connection, list1)
input_new_titles(db_connection, list1)
