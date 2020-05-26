# On the console, type the line above to run the tests
# python manage.py test
import unittest

from django.test import TestCase
from .models import User, Category, MembershipType
from .forms import UserRegistrationForm
from django.core.exceptions import ValidationError

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
    
    def setUp(cls): 
        """
        Setting up the test database (create one category and one membership type)

        """
        category = Category(name='Adherent')
        category.save()
        membership_type = MembershipType.objects.create(name='student')
        membership_type.save()

    def test_create_user(self):
        """
        User can be created with the sign up form if all the mandatory field are correctly filled

        """
        category = Category.objects.all()[0].pk
        data = {'first_name': 'john', 'last_name': 'smith', 'email':'johnsmith@gmail.com', 'password1':'ComplicatedPass1', 'password2':'ComplicatedPass1', 'gender':'M', 'category': category}
        
        form = UserRegistrationForm(data=data)

        self.assertTrue(form.is_valid())
        form.save()

        self.assertIsNotNone(User.objects.get(email='johnsmith@gmail.com'), msg='Testing if the correctly inputted user is created')
        self.assertEqual(User.objects.get(email='johnsmith@gmail.com').email, "johnsmith@gmail.com", msg='Testing if the correctly inputted user is created')

    def test_create_passwordless_user(self):
        """
        User cannot be created with the sign up form if password is empty or is None

        """
        data = {'first_name': 'john', 'last_name': 'smith', 'email':'johnsmith@gmail.com', 'password1':'', 'password2':'', 'gender':'M', 'category': 1}
        
        form = UserRegistrationForm(data=data)

        self.assertFalse(form.is_valid()) #The form is not valid, thus it can't be saved and the user isn't created
        self.assertIsNotNone(User.objects.filter(email='johnsmith@gmail.com'), msg='Testing if the incorrectly inputted user is not created')

        data = {'first_name': 'john', 'last_name': 'smith', 'email':'johnsmith@gmail.com', 'password1':None , 'password2':None, 'gender':'M', 'category': 1}
        
        form = UserRegistrationForm(data=data)

        self.assertFalse(form.is_valid()) #The form is not valid, thus it can't be saved and the user isn't created
        self.assertIsNotNone(User.objects.filter(email='johnsmith@gmail.com'), msg='Testing if the incorrectly inputted user is not created')

    def test_create_user_invalid_email(self):
        """
        User cannot be created with the sign up form if email is empty or invalid

        """
        data = {'first_name': 'john', 'last_name': 'smith', 'email':'johnsmith', 'password1':'ComplicatedPass1', 'password2':'ComplicatedPass1', 'gender':'M', 'category': 1}
        
        form = UserRegistrationForm(data=data)

        self.assertFalse(form.is_valid()) #The form is not valid, thus it can't be saved and the user isn't created
        self.assertIsNotNone(User.objects.filter(email='johnsmith'), msg='Testing if the incorrectly inputted user is not created')


class TestCreateSuperUser(TestCase):
    """
    Tests the create_superuser function on wao/managers.py
    """
    def setUp(cls): 
        """
        Setting up the test database (create one category and one membership type)

        """
        category = Category(name='Adherent')
        category.save()
        membership_type = MembershipType.objects.create(name='student')
        membership_type.save()

    def test_normal_create_superuser(self):
        """
        Tests if the correctly inputted superuser is created

        """
        User.objects.create_superuser(email='superuser_normal@user.com', password="superuser")
        superuser_normal = User.objects.get(email='superuser_normal@user.com')

        self.assertIsNotNone(superuser_normal)
        self.assertTrue(superuser_normal, "superuser_normal@user.com")

    def test_create_passwordless_superuser(self):
        """
        Testing if there is a TypeError  when password is None

        """
        self.assertRaises(TypeError, User.objects.create_superuser, email="superuser_none_password@user.com", password=None)
        self.assertRaises(TypeError, User.objects.create_superuser, email="superuser_none_password@user.com", password="")

    def test_create_superuser_invalid_email(self):
        """
        Testing if there is a TypeError  when a superuser types an empty mail or invalid mail

        """
        self.assertRaises(ValidationError, User.objects.create_user, email="johnsmith", password="superuser")
        self.assertRaises(TypeError, User.objects.create_user, email=None, password="superuser")
        

class TestUser(TestCase):
    """
    Tests that the registration parameters are accessible
    """
    def setUp(cls): 
        """
        Setting up the test database (create one category, one membership type and one user)

        """
        category = Category(name='Adherent')
        category.save()
        membership_type = MembershipType.objects.create(name='student')
        membership_type.save()
        category = Category.objects.all()[0].pk
        data = {'first_name': 'john', 'last_name': 'smith', 'email':'johnsmith@gmail.com', 'password1':'ComplicatedPass1', 'password2':'ComplicatedPass1', 'gender':'M', 'category': category}
        form = UserRegistrationForm(data=data)
        form.save()

    def test_get_last_name(self):
        self.assertEqual(User.objects.get(email='johnsmith@gmail.com').last_name, "smith", msg='Testing if the correctly inputted user is created and is accessible')

    def test_get_first_name(self):
        self.assertEqual(User.objects.get(email='johnsmith@gmail.com').first_name, "john", msg='Testing if the correctly inputted user is created and is accessible')

    def test_email_user(self):
        self.assertEqual(User.objects.get(email='johnsmith@gmail.com').email, "johnsmith@gmail.com", msg='Testing if the correctly inputted user is created and is accessible')

    def test_user_is_not_superuser(self):
        self.assertFalse(User.objects.get(email='johnsmith@gmail.com').is_superuser, msg='Testing if the basic user is not a superuser')


class TestLoginUser(TestCase):
    """
    Tests that the registration parameters are accessible
    """
    def setUp(cls): 
        """
        Setting up the test database (create one category, one membership type and one user)

        """
        category = Category(name='Adherent')
        category.save()
        membership_type = MembershipType.objects.create(name='student')
        membership_type.save()
        category = Category.objects.all()[0].pk
        data = {'first_name': 'john', 'last_name': 'smith', 'email':'johnsmith@gmail.com', 'password1':'ComplicatedPass1', 'password2':'ComplicatedPass1', 'gender':'M', 'category': category}
        form = UserRegistrationForm(data=data)
        form.save()

    def test_user_login(self):    
        response = self.client.post('/login/', {'email':'johnsmith@gmail.com', 'password':'ComplicatedPass1'}, follow=True)
 
        self.assertIsNotNone(response.context['user']) #The user is not None because  the email and password are correct
        self.assertTrue(response.context['user'].is_authenticated) #The user is authenticated
    
    def test_user_incorrect_password(self):
        response = self.client.post('/login/', {'email':'johnsmith@gmail.com', 'password':'IncorrectPassword'}, follow=True)

        self.assertFalse(response.context['user'].is_authenticated) #The user is not authenticated because of incorrect password
        self.assertEqual(response.context[1]["messages"][0]["content"],"Mot de passe incorrect") #The error displayed is the message "Mot de passe incorrect"
    
    def test_user_incorrect_email(self):
        response = self.client.post('/login/', {'email':'johnsmith', 'password':'ComplicatedPass1'}, follow=True)

        self.assertFalse(response.context['user'].is_authenticated) #The user is not authenticated because of incorrect password
        self.assertEqual(response.context[1]["messages"][0]["content"],"E-mail incorrect") #The error displayed is the message "E-mail incorrect"

    # def test_email_user(self):
    #     self.assertEqual(User.objects.get(email='johnsmith@gmail.com').email, "johnsmith@gmail.com", msg='Testing if the correctly inputted user is created and is accessible')

    # def test_user_is_not_superuser(self):
    #     self.assertFalse(User.objects.get(email='johnsmith@gmail.com').is_superuser, msg='Testing if the basic user is not a superuser')


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
