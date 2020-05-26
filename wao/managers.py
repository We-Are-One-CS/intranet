from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
from django.core.validators import validate_email

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """

        if email is None or validate_email(email) is not None:
            raise TypeError('Users must have a valid email address.')

        user = self.model(
            email=self.normalize_email(email),
            birthday=timezone.now()
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):

        if password is None or password == "":
            raise TypeError('Superusers must have a password.')

        if email is None or validate_email(email) is not None:
            raise TypeError('Users must have a valid email address.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user
