import mysql.connector


def view_account_balance(id):
    connection = mysql.connector.connect(host='localhost',
                                         database='banking',
                                         user='root',
                                         password='password')
    cursor = connection.cursor()

    mySql_query = """SELECT currency FROM customers
                            WHERE id = '%s' """ % (id)

    cursor.execute(mySql_query)
    data = cursor.fetchone()
    if not data:
        print("Your ID is not valid! Try again")
    else:
        currency = data[0]
        # print(f"Your account balance has: {currency}$ ")
        return currency
