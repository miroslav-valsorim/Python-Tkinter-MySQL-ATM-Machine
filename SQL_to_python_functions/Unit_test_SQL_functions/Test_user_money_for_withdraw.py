import unittest
import mysql.connector


class TestSQLQueriesCheckAmountBeforeWithdraw(unittest.TestCase):

    def test_user_amount_before_withdraw(self):
        conn = mysql.connector.connect(host="localhost", user="root", passwd="password", database="banking")
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM customers WHERE id = 1 AND currency >= 100") # hardcoded

        result = cursor.fetchone()
        expected = (1,)  # hardcoded to match select statement
        self.assertEqual(result, expected)
        conn.close()


if __name__ == '__main__':
    unittest.main()
