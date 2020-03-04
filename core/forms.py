from django import forms
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField

from .models import User, UserStructure, Event


class DateInput(forms.DateInput):
    input_type = 'date'


class UserRegistrationForm(UserCreationForm):
    telephone = PhoneNumberField(label="Téléphone : ", required=False)
    structures = forms.ModelMultipleChoiceField(
        queryset=UserStructure.objects.all(),
        label='Structures : ',
        help_text="Vous pouvez sélectionner plusieurs éléments",
        required=False
    )
    twitter_link = forms.CharField(label='Lien Twitter : ', required=False)
    linkedin_link = forms.CharField(label='Lien LinkedIn : ', required=False)
    first_name = forms.CharField(label='Prénom : ', required=True)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'telephone',
            'gender',
            'photo',
            'birthday',
            'job_title',
            'structures',
            'cotisation_type',
            'twitter_link',
            'linkedin_link',
            'is_subscribed_newsletter',
            'address',
            'address_complement',
            'zip_code',
            'city',
            'password1',
            'password2'
        )
        labels = {
            'email': 'Email : ',
            'last_name': 'Nom : ',
            'birthday': 'Date de naissance : ',
            'job_title': 'Profession : ',
            'gender': 'Genre : ',
            'photo': 'Photo de profil',
            'is_subscribed_newsletter': 'Je souhaite m\'inscrire à la newsletter',
            'address': 'Addresse : ',
            'address_complement': 'Complément d\'addresse : ',
            'zip_code': 'Code postal : ',
            'city': 'Ville : ',
        }
        widgets = {
            'birthday': DateInput(),
        }


class CompanyRegistrationForm(UserCreationForm):
    telephone = PhoneNumberField(label="Contact téléphonique : ", required=False)
    structures = forms.ModelMultipleChoiceField(
        queryset=UserStructure.objects.all(),
        label='Structures : ',
        help_text="Vous pouvez sélectionner plusieurs éléments",
        required=False
    )
    job_title = forms.CharField(label='Domaine de l\'entreprise : ', required=False, help_text='Par exemple blablabla')
    twitter_link = forms.CharField(label='Lien Twitter : ', required=False)
    linkedin_link = forms.CharField(label='Lien LinkedIn : ', required=False)

    class Meta:
        model = User
        fields = (
            'last_name',
            'email',
            'telephone',
            'job_title',
            'structures',
            'twitter_link',
            'linkedin_link',
            'is_subscribed_newsletter',
            'address',
            'address_complement',
            'zip_code',
            'city',
            'password1',
            'password2'
        )
        labels = {
            'email': 'Email : ',
            'last_name': 'Nom de l\'entreprise : ',
            'is_subscribed_newsletter': 'S\'inscrire à la newsletter',
            'address': 'Addresse : ',
            'address_complement': 'Complément d\'addresse : ',
            'zip_code': 'Code postal : ',
            'city': 'Ville : '
        }
        widgets = {
            'birthday': DateInput(),
        }


class EventCreationForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = (
            'event_title',
            'event_description',
            'event_type',
            'event_date',
            'event_address',
            'event_price',
            'event_capacity',
        )
        labels = {
            'event_title': 'Nom de l\'événement : ',
            'event_description': 'Description : ',
            'event_type': 'Type d\'événement : ',
            'event_date': 'Date de l\'événement : ',
            'event_address': 'Adresse : ',
            'event_price': 'Prix : ',
            'event_capacity': 'Nombre de places : ',
        }
        widgets = {
            'event_date': DateInput(),
        }
