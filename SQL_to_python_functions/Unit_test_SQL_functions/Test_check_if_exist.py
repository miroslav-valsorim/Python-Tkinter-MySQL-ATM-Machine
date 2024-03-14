import unittest
import mysql.connector


class TestSQLQueriesCheckUser(unittest.TestCase):

    def test_check_if_user_exist(self):
        conn = mysql.connector.connect(host="localhost", user="root", passwd="password", database="banking")
        cursor = conn.cursor()
        cursor.execute("SELECT ID, First_Name, Last_Name, PIN FROM customers WHERE ID = 1 and First_name = 'Miroslav' "
                       "and Last_name = 'Hristov' and PIN = 1234")
        result = cursor.fetchall()
        expected = [(1, 'Miroslav', 'Hristov', 1234)]
        self.assertEqual(result, expected)
        conn.close()


if __name__ == '__main__':
    unittest.main()
