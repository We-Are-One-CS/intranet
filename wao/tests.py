# On the console, type the line above to run the tests
# python manage.py test
import unittest

from django.test import TestCase
from .models import User

"""
USERS TESTS
"""


# TEST 1: The registration was well done
# TEST 2: Make a check on the registration parameters
# TEST 3: All required fields are filled in

class TestCreateUser(TestCase):
    """
    Tests the create_user function on wao/managers.py
    """

    def test_normal_create_user(self):
        """
        Tests if the correctly inputted user is subscribed
        """
        user_normal = User.objects.create_user(email='user_normal@user.com', password="user")

        self.assertIsNotNone(User.objects.get(email='user_normal@user.com'),
                             msg='Testing if the correctly inputted user is subscribed')
        self.assertEqual(user_normal.email, "user_normal@user.com",
                         msg='Testing if the correctly inputted user is subscribed')

    def test_passwordless_create_user(self):
        """
        TODO : these tests bugged, because we cannot access the passwords.
        TODO : Check if these tests commented below are needed
        """
        user_empty_password = User.objects.create_user(email="user_empty_password@user.com", password="")
        user_none_password = User.objects.create_user(email="user_none_password@user.com", password=None)
        # self.assertIsNone(user_empty_password.password,
        #                  msg="Testing if user has no password if his password input is ''.")

        # self.assertIsNone(user_none_password.password,
        #                  msg="Testing if user has no password if his password input is not inputted.")

    def test_emailless_create_user(self):
        """
        #Testing if when a user types an empty mail or invalid mail, there is a TypeError
        """

        self.assertRaises(TypeError, User.objects.create_user, email=None, passord="user")
        self.assertRaises(TypeError, User.objects.create_user, email=None, passord=None)


class TestCreateSupeUser(TestCase):
    """
    Tests the create_superuser function on wao/managers.py
    """

    def test_normal_create_superuser(self):
        """
        Tests if the correctly inputted superuser is subscribed
        """

        User.objects.create_superuser(email='superuser_normal@user.com', password="superuser")
        superuser_normal = User.objects.get(email='superuser_normal@user.com')
        self.assertIsNotNone(superuser_normal)
        self.assertTrue(superuser_normal, "superuser_normal@user.com")

    def test_passwordless_create_superuser(self):
        # Testing if there is a TypeError  when a user types an empty or invalid password
        self.assertRaises(TypeError, User.objects.create_superuser,
                          email="superuser_none_password@user.com", password=None)

    def test_emailless_create_superuser(self):
        # Testing if there is a TypeError  when a superuser types an empty mail or invalid mail
        self.assertRaises(TypeError, User.objects.create_superuser,
                          email=None, password="superuser")


# TODO: Finalize these tests
# class TestUser(TestCase):
#     def test_get_full_name(self): # TODO
#         self.fail("Test not yet completed")
#
#     def test_get_short_name(self): # TODO
#         self.fail("Test not yet completed")
#
#     def test_email_user(self): # TODO
#         self.fail("Test not yet completed")
#
#
# class TestViews(TestCase): # TODO
#     def test_error(self):
#         self.fail("Test not yet completed")
#
#     def test_index(self): # TODO
#         self.fail("Test not yet completed")


"""
EVENTS

"""
# TEST 4: The creation was well done
# TEST 5: Make a check on the creation parameters
# TEST 6: All required fields are filled in
# TEST 7: The same applies to the validation and modification of functionality.
# TEST 8: Missing events
# TEST 9: See if it displays more than what was requested
# TEST 10: See if it displays all the personal events
# TEST 11: View secure connection
# TEST 12: Confirmation of payment
# TEST 13: Do not display past events
# TEST 14: Publication well done

# TODO: Finalize these tests
# class TestUser(TestCase): # TODO
#     def test_get_full_name(self): # TODO
#         self.fail("Test not yet completed")
#
#     def test_get_short_name(self): # TODO
#         self.fail("Test not yet completed")
#
#     def test_email_user(self): # TODO
#         self.fail("Test not yet completed")

"""
DEV PROGRAMS

"""
# TEST 15: The registration was well done
# TEST 16 Make a check on the registration parameters
# TEST 17: All required fields are filled in
# TEST 18: Validation well done
# TEST 19: Do all the programs display properly?
# TEST 20: Are you a subscriber (was it well done ?)


"""
YEARBOOK

"""
# TEST 21: The change was well made
# TEST 22: Make a check on the parameters of the change
# TEST 23: All required fields are filled in
# TEST 24: Validation well done
# TEST 25: Filtering works well
# TEST 26: Group has been well established
# TEST 27: Global view well displayed
# TEST 28: Confirming the directory profile with the DB

if __name__ == '__main__':
    unittest.main()
