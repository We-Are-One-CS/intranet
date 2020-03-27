from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from .managers import CustomUserManager


# TODO: Use the standard of models in order to better write all of our models
# https://simpleisbetterthancomplex.com/tips/2018/02/10/django-tip-22-designing-better-models.html

def upload_to_name(instance, filename):
    return 'core/static/core/profile_pictures/' + filename  # A CHANGER EN 'static/core/profile_pictures/' EN PROD !!!


def upload_to_name_event(instance, filename):
    return 'core/static/core/event_pictures/' + filename  # A CHANGER EN 'static/core/event_pictures/' EN PROD !!!


# Create your models here.

class SubjectImpact(models.Model):
    """
    If the person is engaged in WAO Impact, then they are attached to a
    subject that is one of the ODD of ONU that we address.
    Today (March 20, 2020), it will be:
        1. Equal opportunity;
        2. Climate Action;
        3. Health;
        4. Quality Education;
        5. Gender Equality.
    """

    class Meta:
        verbose_name = "Sujet d'impact"
        verbose_name_plural = "Sujets d'impact"

    name = models.CharField(unique=True, max_length=300, verbose_name='Nom')

    def __str__(self):
        return self.name


class Beneficiary(models.Model):
    """
    # TODO: Ask for documentation (Call Alexandre)
    """

    class Meta:
        verbose_name = "Beneficiaire"
        verbose_name_plural = "Beneficiaires"

    name = models.CharField(unique=True, max_length=300, verbose_name='Nom')

    def __str__(self):
        return self.name


class Category(models.Model):
    """"
    There are 3 categories of members:
        1. Adherent
        2. Active
        3. Proactive
    that will depend on the implication at We Are One.
    """

    class Meta:
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'

    name = models.CharField(unique=True, max_length=300, verbose_name='Nom')

    def __str__(self):
        return self.name


class Structure(models.Model):
    """"
    This class corresponds to which structure(s) the person belongs to:
        1. Impact;
        2. Think;
        3. Transform;
        4. Community.
    The same person can belong to several structures.
    """

    class Meta:
        verbose_name = 'Structure'
        verbose_name_plural = 'Structures'

    name = models.CharField(unique=True, max_length=300, verbose_name='Nom')

    def __str__(self):
        return self.name


class MembershipType(models.Model):
    """"
    There are different types according to which type of profile we are dealing with (individual or entreprise)
    There are connected via the plateforme HelloAsso.
    For individuals:
        1. Student
        2. Young Pro
        3. Experimented
        4. Senior
    For companies:
        5. Entrepreneur & Asso
        6. Start-up
        7. Enterprise
        8. Corporate
    """

    class Meta:
        verbose_name = 'Cotisation utilisateur'
        verbose_name_plural = 'Types de cotisation utilisateurs'

    name = models.CharField(unique=True, max_length=300, verbose_name='Nom')

    # company_cotisation = models.BooleanField(verbose_name='Pour les entreprises', blank=True)
    def __str__(self):
        return self.name


class Company(models.Model):
    """
    # TODO: Create documentation for company model
    """

    class Meta:
        verbose_name = 'Entreprise'
        verbose_name_plural = 'Entreprises'

    # TO STRING METHOD
    def __str__(self):
        return self.name

    name = models.CharField(max_length=300, blank=True, null=True)
    email = models.EmailField(unique=True)
    telephone = PhoneNumberField(blank=True, null=True)
    birthday = models.DateField('Date de naissance', blank=True, null=True)
    photo = models.FileField(upload_to=upload_to_name,
                             blank=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    membership_type = models.ForeignKey(MembershipType, on_delete=models.CASCADE, blank=True, null=True)
    address_complement = models.CharField(max_length=500, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    twitter_link = models.CharField(max_length=200, blank=True, null=True)
    facebook_link = models.CharField(max_length=200, blank=True, null=True)
    linkedin_link = models.CharField(max_length=200, blank=True, null=True)

    # CHOICES
    PUBLIC_LIMITED_COMPANY = 'PLC'
    PRIVATE_COMPANY_LIMITED = 'LTD'
    LIMITED_LIABILITY_PARTNERSHIP = 'LLP'
    COMPANY_TYPE_CHOICES = (
        (PUBLIC_LIMITED_COMPANY, 'Public limited company'),
        (PRIVATE_COMPANY_LIMITED, 'Private company limited by shares'),
        (LIMITED_LIABILITY_PARTNERSHIP, 'Limited liability partnership'),
    )
    type = models.CharField(max_length=4, choices=COMPANY_TYPE_CHOICES)


class User(AbstractBaseUser):
    """"
    The most important model of our app
    It models the user profile

    Interactions with the platform
        - The registration
        - Validation by Admin
        - Add/Change data
        - Personal events (later)
        - Personal development (later)


    Tests that are mandatory
        - The registration was well done
        - Make a check on the registration parameters
        - All required fiels are filled in


    """

    class Meta:
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'

    first_name = models.CharField(max_length=300, blank=True, null=True)
    last_name = models.CharField(max_length=500)
    email = models.EmailField(unique=True)
    telephone = PhoneNumberField(blank=True, null=True)
    birthday = models.DateField('Date de naissance', blank=True, null=True)
    GENDER_CHOICES = (
        ('M', 'Homme'),
        ('F', 'Femme'),
        ('O', 'Autre / ne se prononce pas')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    photo = models.FileField(upload_to=upload_to_name,
                             blank=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    structure = models.ManyToManyField(Structure, blank=True)
    membership_type = models.ForeignKey(MembershipType, on_delete=models.CASCADE, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    membership_paid = models.BooleanField(default=False)
    twitter_link = models.CharField(max_length=200, blank=True, null=True)
    facebook_link = models.CharField(max_length=200, blank=True, null=True)
    linkedin_link = models.CharField(max_length=200, blank=True, null=True)
    is_subscribed_newsletter = models.BooleanField(default=False)
    address = models.CharField(max_length=500, blank=True, null=True)
    address_complement = models.CharField(max_length=500, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    # Required fields to extend AbstractBaseUser
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        Not working for now
        """
        # send_mail(subject, message, from_email, [self.email], **kwargs)


class Event(models.Model):
    """"
    The event model models the required fields for event creation
    Events need to be validated by any admin

    Interactions with the platform
        - Proposal/Creation and Delete
        - Validation by Admin
        - Add/Change data
        - View all events/Filter
        - Personal events (later)
        - Pay for events (later)
        - Like/Interest/Participate (later)
        - Publications on the event (later)

    Tests that are mandatory
        - The creation was well done
        - Make a check on the creation parameters
        - All required fields are filled in
        - The same applies to the validation and modification of functionality.
        - Missing events
        - See if it displays more than what was requested
        - See if it displays all the personal events
        - View secure connection
        - Confirmation of payment
        - Do not display past events
        - Publication well done

    """

    class Meta:
        verbose_name = 'Evénement'
        verbose_name_plural = 'Evénements'

    description = models.CharField(max_length=500)
    begin_date = models.DateTimeField("Date de début de l'événement")
    end_date = models.DateTimeField("Date de fin de l'évènement")
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    price = models.FloatField()
    capacity = models.IntegerField()
    type = models.CharField(max_length=100)
    publication_date = models.DateTimeField(name="Date de création de l'évènement", auto_now_add=True)
    photo = models.FileField(upload_to=upload_to_name_event, blank=True)
    is_private = models.BooleanField(
        default=False)  # This is used to know whether normal users will see the event or not
    validated = models.BooleanField(default=False)  # The admin needs to check the event in order to show it

    def __str__(self):
        return self.title


class Yearbook:
    """
    Interactions with the platform
        - Change by Admin
        - Search for profiles
        - Filter
        - Creation of groups
        - Validation of groups by the admin
        - An overview of some profiles
        - Changing group information

    Tests that are mandatory
        - The change was well made
        - Make a check on the parameters of the change
        - All required fields are filled in
        - Validation well done
        - Filtering works well
        - Group has been well established
        - Global view well displayed
        - Confirming the directory profile with the DB

    """
    pass


class SelfDevelopmentProgram:
    """"
    The dev program model models the required fields for dev programs creation
    dev programs need to be validated by any admin

    Interactions with the platform
        - Registration
        - Validation by Admin
        - Subscribe or not
        - Displaying personal programs

    Tests that are mandatory
        - The registration was well done
        - Make a check on the registration parameters
        - All required fields are filled in
        - Validation well done
        - Do all the programs display properly?
        - Are you a subscriber (was it well done ?)

    """
    pass
