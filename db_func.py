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
    result_list = []
    for title in list_of_flats:
        cur.execute("SELECT * FROM flats WHERE title=?", (title[0],))
        rows = cur.fetchall()
        print(rows, title)
        if not len(rows):
            result_list.append(title)

    return result_list


def input_new_titles(conn, list_of_flats):
    cur = conn.cursor()

    # for title in list_of_flats:
    #     cur.execute("INSERT INTO flats (title) VALUES (?)", (title,))
    #     conn.commit()
    cur.executemany("INSERT INTO flats VALUES (?)", list_of_flats)
    conn.commit()
