import mysql
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="banking")


#                              DATABASE CREATION AND PRINTING DATABASES
# my_database = mydb.cursor()
# my_database.execute("Create database Banking")
# my_database.execute("Show databases")
#
# for db in my_database:
#     print(db)


#                              DATABASE TABLE CREATION AND PRINTING OUT TABLES
# my_database = mydb.cursor()
# my_database.execute("CREATE TABLE customers(ID INT AUTO_INCREMENT PRIMARY KEY, First_Name VARCHAR(255), Last_Name "
#                     "VARCHAR(255),Currency INT(200), PIN INT(4), registered DATETIME NOT NULL DEFAULT "
#                     "CURRENT_TIMESTAMP)")
#
# my_database.execute("Show tables")
#
# for tb in my_database:
#     print(tb)


#                              DATABASE IMPORTING VALUES INTO OUR TABLE
# my_database = mydb.cursor()
# sql = "INSERT INTO customers (first_name, last_name, currency, pin) VALUES (%s, %s, %s, %s)"
# val = ("Miroslav", "Hristov", "0", "1234")
# val = ("Miroslav", "Miroslavov", "0", "4321")
# val = ("Hristo", "Hristov", "0", "9876")
# val = ("Hristo", "Miroslavov", "0", "6789")
# val = ("Petyr", "Petrov", "0", "2323")
# val = ("Ivan", "Ivanov", "0", "4545")
# val = ("Georgi", "Georgiev", "0", "9909")
# val = ("Dimitur", "Dimitrov", "0", "1111")
# my_database.execute(sql, val)
# mydb.commit()

