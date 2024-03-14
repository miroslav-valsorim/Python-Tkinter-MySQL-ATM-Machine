class User:
    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    # Ensure ID isn't empty and contains only numbers
    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, value):
        if value == '':
            raise ValueError("Field can't be empty")
        elif not value.isdigit():
            raise ValueError("ID contains only numbers")

        self.__user_id = value

    # Ensure first_name is not empty and it has only letters
    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        if value == '':
            raise ValueError("Field can't be empty")
        elif not value.isalpha():
            raise ValueError("First name should contain only letters")

        self.__first_name = value

    # Ensure last_name is not empty and it has only letters
    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if value == '':
            raise ValueError("Field can't be empty")
        elif not value.isalpha():
            raise ValueError("Last name should contain only letters")

        self.__last_name = value

    def show_details(self):
        return (f"Personal Details\n"
                f"\n"
                f"First Name: {self.first_name}\n"
                f"Last Name: {self.last_name}\n"
                f"ID: {self.user_id}")
