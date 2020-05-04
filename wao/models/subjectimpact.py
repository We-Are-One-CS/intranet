from django.db import models


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

    # CHOICES

    # DATABASE FIELDS
    name = models.CharField(unique=True, max_length=300, verbose_name='Nom')

    # MANAGERS

    # META CLASS
    class Meta:
        verbose_name = "Sujet d'impact"
        verbose_name_plural = "Sujets d'impact"

    # TO STRING METHOD
    def __str__(self):
        return self.name

    # SAVE METHOD

    # ABSOLUTE URL METHOD

    # OTHER METHODS
