from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, UserStructure, UserCotisationType
from phonenumber_field.formfields import PhoneNumberField

class DateInput(forms.DateInput):
    input_type = 'date'

class UserRegistrationForm(UserCreationForm):
    telephone = PhoneNumberField(label="Téléphone : ", required=False)
    structures = forms.ModelMultipleChoiceField(
        queryset= UserStructure.objects.all(), 
        label = 'Structures : ',
        help_text= "Vous pouvez sélectionner plusieurs éléments",
        required= False
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
        queryset= UserStructure.objects.all(), 
        label = 'Structures : ',
        help_text= "Vous pouvez sélectionner plusieurs éléments",
        required= False
        )
    job_title = forms.CharField(label= 'Domaine de l\'entreprise : ', required=False, help_text='Par exemple blablabla')
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

class EventCreationForm(forms.Form):
    event_title = forms.CharField(label='event_name', max_length=100)
    # event_description = models.CharField(max_length=500)
    # event_begin_date = models.DateTimeField("Date de début de l'événement")
    # event_end_date = models.DateTimeField("Date de fin de l'évènement")
    # event_price = models.FloatField()
    # event_capacity = models.IntegerField()
    # event_address = models.CharField(max_length=300)


