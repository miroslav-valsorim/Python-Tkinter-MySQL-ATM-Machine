import mysql.connector


def check_if_client_already_exist(id,first_name, last_name, PIN):
    connection = mysql.connector.connect(host='localhost',
                                         database='banking',
                                         user='root',
                                         password='password')
    cursor = connection.cursor()

    mySql_query = """SELECT ID, First_Name, Last_Name, PIN FROM customers
                     WHERE id = '%s' and first_name = '%s' and last_name = '%s' and pin = '%s'""" % (id, first_name, last_name, PIN)

    cursor.execute(mySql_query)
    data = cursor.fetchall()
    if not data:
        return False
    else:
        return True
