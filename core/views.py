from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, CompanyRegistrationForm


class IndexView(generic.ListView):
    template_name = 'core/index.html'

    def index(request):
        """"
        Temporary solution while we do not construct the queryset method
        """
        return render(request, 'core/index.html')

    # def get_queryset(self):
    #     """"
    #
    #     """
    #     return


class RegisterView:

    def register(request):
        context = {}
        if request.POST:
            if 'user_registration' in request.POST:
                form = UserRegistrationForm(request.POST)
                if form.is_valid():
                    incomplete_user = form.save(commit=False)
                    incomplete_user.is_enterprise = False
                    incomplete_user.is_active = False
                    email = form.cleaned_data.get('email')
                    raw_password = form.cleaned_data.get('password1')
                    incomplete_user.save()
                    login(request, incomplete_user, backend='django.contrib.auth.backends.ModelBackend')
                    return redirect('index')
                else:
                    context['user_registration_form'] = form
            elif 'company_registration' in request.POST:
                form = CompanyRegistrationForm(request.POST)
                if form.is_valid():
                    user = form.save(commit=False)
                    cotisation_id = user.cotisation_type
                    print(cotisation_id)
                    user.is_enterprise = True
                    user.is_active = False
                    email = form.cleaned_data.get('email')
                    raw_password = form.cleaned_data.get('password1')
                    user.save()
                    login(request, incomplete_user, backend='django.contrib.auth.backends.ModelBackend')
                    return redirect('index')
        else:
            user_form = UserRegistrationForm()
            context['user_registration_form'] = user_form
            company_form = CompanyRegistrationForm()
            context['company_registration_form'] = company_form
        return render(request, 'core/register.html', context)


class EventsView(generic.ListView):
    template_name = 'core/events.html'

    def events(request):
        """"
        Temporary solution while we do not construct the queryset method
        """
        return render(request, 'core/events.html')


class CreateEventView(generic.ListView):
    template_name = 'core/create_event.html'

    def create_event(request):
        """"
        Temporary solution while we do not construct the queryset method
        """
        return render(request, 'core/create_event.html')


class AllEventsView(generic.ListView):
    template_name = 'core/all_events.html'

    def all_events(request):
        """"
        Temporary solution while we do not construct the queryset method
        """
        return render(request, 'core/all_events.html')


class SearchEventsView(generic.ListView):
    template_name = 'core/search_events.html'

    def search_events(request):
        """"
        Temporary solution while we do not construct the queryset method
        """
        return render(request, 'core/search_events.html')


class SubscribeEventsView(generic.ListView):
    template_name = 'core/subscribe_events.html'

    def subscribe_events(request):
        """"
        Temporary solution while we do not construct the queryset method
        """
        return render(request, 'core/subscribe_events.html')


class YearbookView(generic.ListView):
    template_name = 'core/yearbook.html'

    def yearbook(request):
        """"
        Temporary solution while we do not construct the queryset method
        """
        return render(request, 'core/yearbook.html')


class ProgramsView(generic.ListView):
    template_name = 'core/programs.html'

    def programs(request):
        """"
        Temporary solution while we do not construct the queryset method
        """
        return render(request, 'core/programs.html')


class UserView(generic.ListView):

    def user(request):
        """"
        Temporary solution while we do not construct the queryset method
        """
        return render(request, 'core/user.html')
