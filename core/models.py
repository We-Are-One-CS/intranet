from django.db import models
from django.utils import timezone


# Create your models here.

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    active_account = models.BooleanField()
    user_first_name = models.CharField(max_length=300)
    user_last_name = models.CharField(max_length=500)
    user_mail = models.EmailField()
    user_telephone = models.IntegerField()
    user_birthday = models.DateTimeField('Date de naissance')
    # user_photo = models.ImageField("Photo de l'utilisateur") # I did not get the website to work when I added this
    user_job_title = models.CharField(max_length=100)
    user_categories = models.CharField(max_length=300)
    user_structure = models.CharField(max_length=100)
    user_is_enterprise = models.BooleanField()


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
