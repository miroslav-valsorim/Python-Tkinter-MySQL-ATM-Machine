import unittest
import mysql.connector


class TestSQLQueriesInsertNewUser(unittest.TestCase):

    # in order this test to work, variables in first query and expected results should be hardcoded
    # to the values to match database results before and after 1st query execution
    def test_insert_new_user(self):
        connection = mysql.connector.connect(host="localhost", user="root", passwd="password", database="banking")
        cursor = connection.cursor()

        # Action
        mySql_query = """INSERT INTO customers (First_Name, Last_Name, Currency, PIN)
                                        VALUES ('Jerard','Gogovov',0,1234)  """  # hardcoded
        cursor.execute(mySql_query)
        connection.commit()

        # getting result after action
        mySql_query = """SELECT ID, First_Name, Last_Name, Currency, PIN FROM customers
                                    WHERE First_name = 'Jerard' and Last_name = 'Gogovov' 
                                    and Currency = 0 and PIN = 1234"""  # hardcoded
        cursor.execute(mySql_query)

        result = cursor.fetchall()
        expected = ([(18, 'Jerard', 'Gogovov', 0, 1234)]) # hardcoded

        self.assertEqual(result, expected)
        connection.close()


if __name__ == '__main__':
    unittest.main()
