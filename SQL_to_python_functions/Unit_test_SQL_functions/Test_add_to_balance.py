import unittest
import mysql.connector


class TestSQLQueriesAddCurrency(unittest.TestCase):

    # in order this test to work, variables like ID on first query and expected results should be hardcoded
    # to the values to match database results before and after 1st query execution
    def test_add_currency_to_user(self):
        connection = mysql.connector.connect(host="localhost", user="root", passwd="password", database="banking")
        cursor = connection.cursor()

        # Action
        mySql_query = """UPDATE customers
                        SET currency = currency + 100 
                         WHERE id = 1 """  # +100 and ID hardcoded
        cursor.execute(mySql_query)
        connection.commit()

        # getting result after action
        mySql_query = """SELECT currency FROM customers
                                    WHERE id = 1 """  # ID hardcoded
        cursor.execute(mySql_query)

        result = cursor.fetchone()
        expected = (1360,)

        self.assertEqual(result, expected)
        connection.close()


if __name__ == '__main__':
    unittest.main()
