import mysql.connector


def get_new_user_id():
    connection = mysql.connector.connect(host='localhost',
                                         database='banking',
                                         user='root',
                                         password='password')
    cursor = connection.cursor()

    mySql_query = """SELECT id FROM customers ORDER BY ID DESC LIMIT 1"""
    # mySql_query = """SELECT LAST_INSERT_ID()"""

    cursor.execute(mySql_query)
    data = cursor.fetchone()
    if not data:
        return 1
    else:
        new_id = data[0]
        return new_id
