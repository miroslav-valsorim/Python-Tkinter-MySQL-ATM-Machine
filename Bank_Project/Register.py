
class Register:
    def __init__(self, first_name, last_name, pin):
        self.first_name = first_name
        self.last_name = last_name
        self.pin = pin

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
