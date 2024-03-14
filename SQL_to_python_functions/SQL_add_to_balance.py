import mysql.connector


def add_currency_to_user(id, amount):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='banking',
                                             user='root',
                                             password='password')
        cursor = connection.cursor()

        mySql_query = """UPDATE customers
                         SET currency = currency + '%s' 
                        WHERE id = '%s' """ % (amount, id)

        cursor.execute(mySql_query)
        connection.commit()
        return f"{amount}$ were added to your currency"

    except mysql.connector.Error as error:
        return "Something went wrong, please try again later"

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection is closed")
