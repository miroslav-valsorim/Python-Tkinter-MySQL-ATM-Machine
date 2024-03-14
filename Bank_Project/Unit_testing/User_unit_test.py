from unittest import TestCase, main
from Bank_Project.User import User


class TestUser(TestCase):

    def setUp(self):
        self.bank_user = User("15", "John", "Lee")

    def test_initializing(self):
        self.assertEqual("15", self.bank_user.user_id)
        self.assertEqual("John", self.bank_user.first_name)
        self.assertEqual("Lee", self.bank_user.last_name)

    def test_empty_user_id(self):
        with self.assertRaises(ValueError) as ve:
            self.bank_user.user_id = ""

        self.assertEqual("Field can't be empty", str(ve.exception))

    def test_user_id_with_other_than_num(self):
        with self.assertRaises(ValueError) as ve:
            self.bank_user.user_id = "eaa"

        self.assertEqual("ID contains only numbers", str(ve.exception))

    def test_empty_user_first_name(self):
        with self.assertRaises(ValueError) as ve:
            self.bank_user.first_name = ""

        self.assertEqual("Field can't be empty", str(ve.exception))

    def test_first_name_with_other_than_letters(self):
        with self.assertRaises(ValueError) as ve:
            self.bank_user.first_name = "1234"

        self.assertEqual("First name should contain only letters", str(ve.exception))

    def test_empty_user_last_name(self):
        with self.assertRaises(ValueError) as ve:
            self.bank_user.last_name = ""

        self.assertEqual("Field can't be empty", str(ve.exception))

    def test_last_name_with_other_than_letters(self):
        with self.assertRaises(ValueError) as ve:
            self.bank_user.last_name = "1234"

        self.assertEqual("Last name should contain only letters", str(ve.exception))

    def test_first_name_getter(self):
        self.assertEqual(self.bank_user.first_name, "John")

    def test_last_name_getter(self):
        self.assertEqual(self.bank_user.last_name, "Lee")

    def test_id_getter(self):
        self.assertEqual(self.bank_user.user_id, "15")

    def test_show_details(self):
        self.bank_user.show_details()
        self.assertEqual(f"Personal Details\n"
                         f"\n"
                         f"First Name: John\n"
                         f"Last Name: Lee\n"
                         f"ID: 15", self.bank_user.show_details())


if __name__ == "__main__":
    main()
