from django.db import models


class Structure(models.Model):
    """"
    This class corresponds to which structure(s) the person belongs to:
        1. Impact;
        2. Think;
        3. Transform;
        4. Community.
    The same person can belong to several structures.
    """

    # CHOICES

    # DATABASE FIELDS
    name = models.CharField(unique=True, max_length=300, verbose_name='Nom')

    # MANAGERS

    # META CLASS
    class Meta:
        verbose_name = 'Structure'
        verbose_name_plural = 'Structures'

    # TO STRING METHOD
    def __str__(self):
        return self.name

    # SAVE METHOD

    # ABSOLUTE URL METHOD

    # OTHER METHODS
