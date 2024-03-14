from Bank_Project.Bank import Bank
from Bank_Project.Register import Register
from SQL_to_python_functions.SQL_check_if_exists import check_if_client_already_exist
from Bank_Project.Additional_functionality import register_new_customer, user_options


# LOGIN - REGISTER
#    Main menu
while True:
    options = input(
        "\n\n**** Welcome to our Bank ****\n\n"
        "Enter one of the following down commands (enter a number)\n\n"
        "1. Login\n"
        "2. Register\n\n"
        ">>"
    )

    if options == '1':
        user = Bank(input("\nEnter ID: "),
                    input("Enter First Name: "),
                    input("Enter Last Name: "),
                    input("Enter PIN: "))

        if check_if_client_already_exist(user.user_id, user.first_name, user.last_name, user.pin) is True:
            user_options(user)
            break
        else:
            raise Exception("Your details dont match, try again")

    elif options == '2':
        register_user = Register(input("\nSet your First Name: "),
                                 input("Set your Last Name: "),
                                 input("Set your PIN (Should contains only 4 numbers!): "))

        try:
            register_new_customer(register_user.first_name, register_user.last_name, 0, register_user.pin)
            break
        except:
            raise Exception("Something went wrong, please try again later or contact our support")

    else:
        print("Please enter valid number")


