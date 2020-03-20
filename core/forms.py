from django import forms
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField

from .models import User, Structure, Event


class DateInput(forms.DateInput):
    input_type = 'date'


class UserRegistrationForm(UserCreationForm):
    telephone = PhoneNumberField(label="Téléphone : ", required=False)
    structures = forms.ModelMultipleChoiceField(
        queryset=Structure.objects.all(),
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
            'structure',
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
        queryset=Structure.objects.all(),
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
            'structure',
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
    title = forms.CharField(label='Nom de l\'événement : ', required=True)

    class Meta:
        model = Event
        fields = (
            'title',
            'description',
            'type',
            'begin_date',
            'end_date',
            'address',
            'price',
            'capacity',
            'photo',
        )
        labels = {
            'title': 'Nom de l\'événement : ',
            'description': 'Description : ',
            'type': 'Type d\'événement : ',
            'begin_date': 'Date de début l\'événement : ',
            'end_date': 'Date de fin l\'événement : ',
            'address': 'Adresse : ',
            'price': 'Prix : ',
            'capacity': 'Nombre de places : ',
            'photo': 'Photo de l\'événement',
        }
        widgets = {
            'begin_date': DateInput(),
            'end_date': DateInput(),
        }
