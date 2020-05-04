from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from .membership_type import MembershipType


def upload_to_name(instance, filename):
    return 'wao/static/wao/profile_pictures/' + filename  # A CHANGER EN 'static/wao/profile_pictures/' EN PROD !!!


class Company(models.Model):
    """
    # TODO: Create documentation for company model
    """

    # CHOICES
    PUBLIC_LIMITED_COMPANY = 'PLC'
    PRIVATE_COMPANY_LIMITED = 'LTD'
    LIMITED_LIABILITY_PARTNERSHIP = 'LLP'
    COMPANY_TYPE_CHOICES = (
        (PUBLIC_LIMITED_COMPANY, 'Public limited company'),
        (PRIVATE_COMPANY_LIMITED, 'Private company limited by shares'),
        (LIMITED_LIABILITY_PARTNERSHIP, 'Limited liability partnership'),
    )

    # DATABASE FIELDS
    type = models.CharField(max_length=4, choices=COMPANY_TYPE_CHOICES)
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

    # MANAGERS

    # META CLASS
    class Meta:
        verbose_name = 'Entreprise'
        verbose_name_plural = 'Entreprises'

    # TO STRING METHOD
    def __str__(self):
        return self.name

    # SAVE METHOD

    # ABSOLUTE URL METHOD

    # OTHER METHODS
