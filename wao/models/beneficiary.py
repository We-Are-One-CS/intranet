from django.db import models


class Beneficiary(models.Model):
    """
    # TODO: Ask for documentation (Call Alexandre)
    """

    # CHOICES

    # DATABASE FIELDS
    name = models.CharField(unique=True, max_length=300, verbose_name='Nom')

    # MANAGERS

    # META CLASS
    class Meta:
        verbose_name = "Beneficiaire"
        verbose_name_plural = "Beneficiaires"

    # TO STRING METHOD
    def __str__(self):
        return self.name

    # SAVE METHOD

    # ABSOLUTE URL METHOD

    # OTHER METHODS
