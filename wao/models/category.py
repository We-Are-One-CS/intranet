from django.db import models


class Category(models.Model):
    """"
    There are 3 categories of members:
        1. Adherent
        2. Active
        3. Proactive
    that will depend on the implication at We Are One.
    """

    # CHOICES

    # DATABASE FIELDS
    name = models.CharField(unique=True, max_length=300, verbose_name='Nom')

    # MANAGERS

    # META CLASS
    class Meta:
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'

    # TO STRING METHOD

    # SAVE METHOD
    def __str__(self):
        return self.name

    # ABSOLUTE URL METHOD

    # OTHER METHODS
