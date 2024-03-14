import unittest
import mysql.connector


class TestSQLQueriesViewAccountBalance(unittest.TestCase):

    def test_view_account_balance(self):
        connection = mysql.connector.connect(host="localhost", user="root", passwd="password", database="banking")
        cursor = connection.cursor()

        cursor.execute("SELECT currency FROM customers WHERE id = 1 ")

        result = cursor.fetchone()
        expected = (1260,)  # hardcoded value

        self.assertEqual(result, expected)
        connection.close()


if __name__ == '__main__':
    unittest.main()
