from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import CustomUserManager
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class UserCategory(models.Model):
    class Meta:
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'
    name = models.CharField(unique=True, max_length=300, verbose_name='Nom')
    def __str__(self):
        return self.name

class UserStructure(models.Model):
    class Meta:
        verbose_name = 'Structure'
        verbose_name_plural = 'Structures'
    name = models.CharField(unique=True, max_length=300, verbose_name='Nom')
    def __str__(self):
        return self.name

class UserCotisationType(models.Model):
    class Meta:
        verbose_name = 'Cotisation utilisateur'
        verbose_name_plural = 'Types de cotisation utilisateurs'
    name = models.CharField(unique = True, max_length=300, verbose_name='Nom')
    cotisation_user = models.BooleanField()     
    # company_cotisation = models.BooleanField(verbose_name='Pour les entreprises', blank=True)
    def __str__(self):
        return self.name

class User(AbstractBaseUser):
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
    # photo = models.ImageField("Photo de l'utilisateur") # I did not get the website to work when I added this
    job_title = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(UserCategory, on_delete=models.CASCADE, default=1)
    structures = models.ManyToManyField(UserStructure, blank=True)
    is_enterprise = models.BooleanField()
    cotisation_type = models.ForeignKey(UserCotisationType, on_delete=models.CASCADE, default=1)
    twitter_link = models.CharField(max_length=200, blank=True, null=True)
    linkedin_link = models.CharField(max_length=200, blank=True, null=True)
    is_subscribed_newsletter = models.BooleanField(default=False)
    address = models.CharField(max_length=500, blank=True, null=True)
    address_complement = models.CharField(max_length=500, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    # Required fields to extend AbstractBaseUser
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class Event(models.Model):
    event_id = models.IntegerField(primary_key=True)
    event_description = models.CharField(max_length=500)
    publication_date = models.DateTimeField('Date de publication')
    event_date = models.DateTimeField("Date de l'événement")
    event_title = models.CharField(max_length=100)
    event_address = models.CharField(max_length=300)
    event_price = models.FloatField()
    event_capacity = models.IntegerField()
    event_type = models.CharField(max_length=100)
    # event_photo = models.ImageField("Photo de l'événement") # I don't know if it works
    # event_is_private = models.BooleanField() # I don't know if it has to be here
    # event_is_valide = models.BooleanField() # I don't know if it has to be here


class SelfDevelopmentProgram:
    pass


class Yearbook:
    pass
