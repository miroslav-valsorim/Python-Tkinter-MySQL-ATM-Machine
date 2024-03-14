from User import User

from SQL_to_python_functions.SQL_check_if_exists import check_if_client_already_exist
from SQL_to_python_functions.SQL_add_to_balance import add_currency_to_user
from SQL_to_python_functions.SQL_check_user_money_for_withdraw import \
    check_if_user_has_the_current_amount_of_money_to_withdraw
from SQL_to_python_functions.SQL_remove_curent_amount_from_balance import remove_currency_from_user
from SQL_to_python_functions.SQL_view_account_balance import view_account_balance


class Bank(User):
    def __init__(self, user_id, first_name, last_name, pin):
        super().__init__(user_id, first_name, last_name)
        self.pin = pin

    # Ensure pin has only 4 numbers
    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, value):
        if value == '':
            raise ValueError("Field can't be empty")
        elif not value.isdigit():
            raise ValueError("PIN should contain only numbers")
        elif len(str(value)) != 4:
            raise ValueError("PIN should have 4 digits")

        self.__pin = value

    def deposit(self, amount):
        if check_if_client_already_exist(self.user_id, self.first_name, self.last_name, self.pin) is True:
            print(add_currency_to_user(self.user_id, amount))

    def withdraw(self, amount):
        if check_if_user_has_the_current_amount_of_money_to_withdraw(self.user_id, amount) is False:
            print("\nYou don't have enough currency to withdraw")
            print(view_account_balance(self.user_id))

        else:
            print(remove_currency_from_user(self.user_id, amount))

    def view_balance(self):
        return f"Your account balance has: {view_account_balance(self.user_id)}$"
