import unittest
import mysql.connector


class TestSQLQueriesNewUserId(unittest.TestCase):

    def test_new_user_id_or_last_added_id(self):
        conn = mysql.connector.connect(host="localhost", user="root", passwd="password", database="banking")
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM customers ORDER BY ID DESC LIMIT 1")

        result = cursor.fetchone()
        expected = (18, )
        self.assertEqual(result, expected)
        conn.close()


if __name__ == '__main__':
    unittest.main()
