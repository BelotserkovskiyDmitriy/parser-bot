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
    for item in list_of_flats:
        cur.execute("SELECT title FROM flats WHERE title=?", (item[0],))
        rows = cur.fetchall()
        if not len(rows):
            result_list.append(item)

    return result_list


def input_new_titles(conn, list_of_flats):
    cur = conn.cursor()

    sql = ''' INSERT INTO flats(title, flats_id)
              VALUES(?, ?) '''
    for flat in list_of_flats:
        cur.execute(sql, (flat['url'], flat['object_id']))
    conn.commit()


def search_by_id(conn, flats_id):
    cur = conn.cursor()

    cur.execute("SELECT title FROM flats WHERE flats_id=?", (flats_id,))
    rows = cur.fetchall()

    return rows
