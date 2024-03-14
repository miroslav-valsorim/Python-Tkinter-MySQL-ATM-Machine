import mysql.connector


def check_if_user_has_the_current_amount_of_money_to_withdraw(id, amount):
    connection = mysql.connector.connect(host='localhost',
                                         database='banking',
                                         user='root',
                                         password='password')
    cursor = connection.cursor()

    mySql_query = """SELECT id FROM customers
                         WHERE id = '%s'
                         AND currency >= '%s' """ % (id, amount)

    cursor.execute(mySql_query)
    data = cursor.fetchall()
    if not data:
        return False
    else:
        return True
