from django.db import models

from .user import User


def upload_to_name_event(instance, filename):
    return 'wao/static/wao/event_pictures/' + filename  # A CHANGER EN 'static/wao/event_pictures/' EN PROD !!!


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

    # CHOICES

    # DATABASE FIELDS
    description = models.CharField(max_length=500)
    begin_date = models.DateTimeField("Date de début de l'événement")
    end_date = models.DateTimeField("Date de fin de l'évènement")
    participants = models.ManyToManyField(User)
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
    owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'owner', blank=True, null=True, default=1)


    # MANAGERS

    # META CLASS
    class Meta:
        verbose_name = 'Evénement'
        verbose_name_plural = 'Evénements'

    # TO STRING METHOD
    def __str__(self):
        return self.title

    # SAVE METHOD

    # ABSOLUTE URL METHOD

    # OTHER METHODS
