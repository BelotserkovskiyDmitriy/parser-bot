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
# def update_list(list_of_flats):
#     result_list = []
#     conn = sqlite3.connect("titles.db")
#
#     for item in list_of_flats:
#         cur = conn.cursor()
#         cur.execute("SELECT title FROM projects WHERE title =?;", (item,))
#         rows = cur.fetchall()
#         if not len(rows):
#             result_list.append(item)
#             cur.execute("INSERT INTO projects VALUES(?);", (item,))
#             conn.commit()
#
#     conn.close()
#     return result_list


def input_new_titles(conn, list_of_flats):
    unique_objects = []
    sql = ''' INSERT INTO flats(title, flats_id)
              VALUES(?, ?); '''
    for flat in list_of_flats:
        cur = conn.cursor()
        cur.execute("SELECT * FROM flats WHERE flats_id =?;", (flat['object_id'],))
        rows = cur.fetchall()
        if not len(rows):
            unique_objects.append(flat)

            cur.execute(sql, (flat['url'], flat['object_id']))
            conn.commit()
    return unique_objects


def search_by_id(conn, flats_id):
    cur = conn.cursor()

    cur.execute("SELECT title FROM flats WHERE flats_id=?;", (flats_id,))
    rows = cur.fetchall()

    return rows

# test_list = ["https://www.olx.ua/obyavlenie/sdam-1-komn-kv-holodnaya-gora-novostroy-17min-peshkom-pr-lyubovi-maloy49-IDK35nZ.html#b43a2441f0;promoted", "https://www.olx.ua/obyavlenie/sdam-1k-kv-v-novostroe-elizavetinskaya-3b-IDJ2kyV.html#50d889f15c"]
# conn = create_connection("flats_olx.db")
# print(update_list(conn, test_list))

def create_db_file():
    conn = sqlite3.connect('titles.db')
    cur = conn.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS projects (title TEXT PRIMARY KEY);'
    cur.execute(sql)


# create_db_file()
