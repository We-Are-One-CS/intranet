from django.db import models


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

    # CHOICES

    # DATABASE FIELDS
    name = models.CharField(unique=True, max_length=300, verbose_name='Nom')

    # company_cotisation = models.BooleanField(verbose_name='Pour les entreprises', blank=True)

    # MANAGERS

    # META CLASS
    class Meta:
        verbose_name = 'Cotisation utilisateur'
        verbose_name_plural = 'Types de cotisation utilisateurs'

    # TO STRING METHOD
    def __str__(self):
        return self.name

    # SAVE METHOD

    # ABSOLUTE URL METHOD

    # OTHER METHODS
