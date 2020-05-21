from django.db import models


class EventType(models.Model):
    """"
    This class corresponds to the label(s) that a person can choose when creating an event:
    
    """

    # CHOICES

    # DATABASE FIELDS
    label = models.CharField(unique=True, max_length=300, verbose_name='Label')

    # MANAGERS

    # META CLASS
    class Meta:
        verbose_name = 'Type d\'événements'
        verbose_name_plural = 'Types d\'événements'

    # TO STRING METHOD
    def __str__(self):
        return self.label

    # SAVE METHOD

    # ABSOLUTE URL METHOD

    # OTHER METHODS
