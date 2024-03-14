from SQL_to_python_functions.SQL_insert_to_database import insert_varibles_into_table
from SQL_to_python_functions.SQL_get_new_user_id import get_new_user_id


def register_new_customer(first_name, last_name, currency, pin):
    insert_varibles_into_table(first_name, last_name, currency, pin)
    print("\nYour account has been created!")
    print(f"Your client ID is {get_new_user_id()}")


def cont():
    input("\nPress enter to continue\n")


def user_options(user):
    while True:
        options = input(
            "\nEnter one of the following down commands (enter a number)\n\n"
            "1. Withdraw\n"
            "2. Deposit\n"
            "3. View Account Summary\n"
            "4. View balance\n"
            "5. Exit \n>>")

        if options == '5':
            exit = 1
            break
        if options == '3':
            print(user.show_details())
            cont()
        elif options == '4':
            print(user.view_balance())
            cont()
        elif options == "1":
            user.withdraw(int(input("\nHow much would you like to withdraw?: ")))
            cont()
        elif options == "2":
            user.deposit(int(input("\nHow much would you like to deposit?: ")))
            cont()



