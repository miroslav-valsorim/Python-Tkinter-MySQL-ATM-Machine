import mysql.connector


def insert_varibles_into_table(first_name, last_name, currency, pin):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='banking',
                                             user='root',
                                             password='password')
        cursor = connection.cursor()

        mySql_query = """INSERT INTO customers (First_Name, Last_Name, Currency, PIN)
                                        VALUES ('%s','%s','%s','%s') """ % (first_name, last_name, currency, pin)

        cursor.execute(mySql_query)
        connection.commit()

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            return True
            # print("MySQL connection is closed")
