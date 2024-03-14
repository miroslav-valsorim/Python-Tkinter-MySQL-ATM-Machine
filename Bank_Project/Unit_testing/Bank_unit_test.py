from unittest import TestCase, main
from Bank_Project.Bank import Bank


class TestBank(TestCase):

    def setUp(self):
        self.banking_user = Bank("1", "John", "Lee", "3333")

    def test_initializing(self):
        self.assertEqual("1", self.banking_user.user_id)
        self.assertEqual("John", self.banking_user.first_name)
        self.assertEqual("Lee", self.banking_user.last_name)
        self.assertEqual("3333", self.banking_user.pin)

    def test_empty_pin_value(self):
        with self.assertRaises(ValueError) as ve:
            self.banking_user.pin = ""

        self.assertEqual("Field can't be empty", str(ve.exception))

    def test_pin_with_other_than_numbers(self):
        with self.assertRaises(ValueError) as ve:
            self.banking_user.pin = "qwerty"

        self.assertEqual("PIN should contain only numbers", str(ve.exception))

    def test_pin_with_more_than_four_numbers(self):
        with self.assertRaises(ValueError) as ve:
            self.banking_user.pin = "12345"

        self.assertEqual("PIN should have 4 digits", str(ve.exception))


if __name__ == "__main__":
    main()


