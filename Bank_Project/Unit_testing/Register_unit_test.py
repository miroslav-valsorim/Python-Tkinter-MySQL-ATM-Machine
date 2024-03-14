from unittest import TestCase, main
from Bank_Project.Register import Register


class TestRegister(TestCase):

    def setUp(self):
        self.new_user = Register("John", "Lee", "3333")

    def test_initializing(self):
        self.assertEqual("John", self.new_user.first_name)
        self.assertEqual("Lee", self.new_user.last_name)
        self.assertEqual("3333", self.new_user.pin)

    def test_empty_user_first_name(self):
        with self.assertRaises(ValueError) as ve:
            self.new_user.first_name = ""

        self.assertEqual("Field can't be empty", str(ve.exception))

    def test_first_name_with_other_than_letters(self):
        with self.assertRaises(ValueError) as ve:
            self.new_user.first_name = "1234"

        self.assertEqual("First name should contain only letters", str(ve.exception))

    def test_empty_user_last_name(self):
        with self.assertRaises(ValueError) as ve:
            self.new_user.last_name = ""

        self.assertEqual("Field can't be empty", str(ve.exception))

    def test_last_name_with_other_than_letters(self):
        with self.assertRaises(ValueError) as ve:
            self.new_user.last_name = "1234"

        self.assertEqual("Last name should contain only letters", str(ve.exception))

    def test_empty_pin_value(self):
        with self.assertRaises(ValueError) as ve:
            self.new_user.pin = ""

        self.assertEqual("Field can't be empty", str(ve.exception))

    def test_pin_with_other_than_numbers(self):
        with self.assertRaises(ValueError) as ve:
            self.new_user.pin = "qwerty"

        self.assertEqual("PIN should contain only numbers", str(ve.exception))

    def test_pin_with_more_than_four_numbers(self):
        with self.assertRaises(ValueError) as ve:
            self.new_user.pin = "12345"

        self.assertEqual("PIN should have 4 digits", str(ve.exception))

    def test_first_name_getter(self):
        self.assertEqual(self.new_user.first_name, "John")

    def test_last_name_getter(self):
        self.assertEqual(self.new_user.last_name, "Lee")

    def test_pin_getter(self):
        self.assertEqual(self.new_user.pin, "3333")


if __name__ == "__main__":
    main()
