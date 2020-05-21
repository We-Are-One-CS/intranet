from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from phonenumber_field.formfields import PhoneNumberField
from tempus_dominus.widgets import DateTimePicker

from .models import User, Structure, Event, Category
from multiselectfield import MultiSelectFormField


class DateInput(forms.DateInput):
    input_type = 'date'


class UserRegistrationForm(UserCreationForm):
    telephone = PhoneNumberField(label="Téléphone : ", required=False)
    structure = forms.ModelMultipleChoiceField(
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
            'password1',
            'password2',
            'telephone',
            'gender',
            'photo',
            'birthday',
            'job_title',
            'structure',
            'category',
            'membership_type',
            'twitter_link',
            'linkedin_link',
            'is_subscribed_newsletter',
            'address',
            'address_complement',
            'zip_code',
            'city',
            'country'
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
    structure = forms.ModelMultipleChoiceField(
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
            'category',
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
            'category': 'Catégorie : ',
            'is_subscribed_newsletter': 'S\'inscrire à la newsletter',
            'address': 'Addresse : ',
            'address_complement': 'Complément d\'addresse : ',
            'zip_code': 'Code postal : ',
            'city': 'Ville : ',
            'country': 'Pays :'
        }
        widgets = {
            'birthday': DateInput(),
        }


class EventCreationForm(forms.ModelForm):
    title = forms.CharField(label='Nom de l\'événement : ', required=True)
    begin_date = forms.DateTimeField(input_formats=['%m/%d/%Y %I:%M %p'], label="Date de début de l\'événement",
                                     widget=DateTimePicker(attrs={
                                         'append': 'fa fa-calendar',
                                         'icon_toggle': True, }))
    end_date = forms.DateTimeField(input_formats=['%m/%d/%Y %I:%M %p'], label="Date de fin de l\'évènement",
                                   widget=DateTimePicker(attrs={
                                       'append': 'fa fa-calendar',
                                       'icon_toggle': True, }))

    type = MultiSelectFormField(
        widget= forms.SelectMultiple,
        label='Type d\'événement : ',
        help_text="Vous pouvez sélectionner plusieurs éléments",
        required=False,
        choices = Event.TYPE_CHOICES,
    )

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


class UserUpdateForm(UserChangeForm):
    telephone = PhoneNumberField(label="Téléphone : ", required=False)
    structure = forms.ModelMultipleChoiceField(
        queryset=Structure.objects.all(),
        label='Structures : ',
        help_text="Vous pouvez sélectionner plusieurs éléments",
        required=False
    )
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        label='Catégorie : ',
        help_text="Vous pouvez sélectionner juste une élément !",
        required=True
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
            'category',
            'membership_type',
            'twitter_link',
            'linkedin_link',
            'is_subscribed_newsletter',
            'address',
            'address_complement',
            'zip_code',
            'city',
            'country'
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
