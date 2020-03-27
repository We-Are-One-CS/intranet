from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic

from .forms import EventCreationForm
from .forms import UserRegistrationForm, CompanyRegistrationForm
from .models import User, Event


def error(request, message="Bienvenue sur la page d'affichage d'erreurs !"):
    # This special view is called everytime there is an error to display it into the browser
    return render(request, 'core/error.html', {'messages': request.messages, })


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
        return render(request, 'core/register.html')

    def register_user(request):
        context = {}
        if request.POST:
            if 'user_registration' in request.POST:
                form = UserRegistrationForm(request.POST, request.FILES or None)
                if form.is_valid():
                    incomplete_user = form.save(commit=False)
                    incomplete_user.is_enterprise = False
                    incomplete_user.is_active = False
                    email = form.cleaned_data.get('email')
                    raw_password = form.cleaned_data.get('password1')
                    incomplete_user.save()
                    login(request, incomplete_user, backend='django.contrib.auth.backends.ModelBackend')
                    return redirect('login')
                else:
                    context['user_registration_form'] = form
        else:
            user_form = UserRegistrationForm()
            context['user_registration_form'] = user_form
        return render(request, 'core/register_user.html', context)

    def register_company(request):
        context = {}
        if request.POST:
            if 'company_registration' in request.POST:
                form = CompanyRegistrationForm(request.POST)
                if form.is_valid():
                    user = form.save(commit=False)
                    membership_id = user.membership_type
                    print(membership_id)
                    user.is_enterprise = True
                    user.is_active = False
                    email = form.cleaned_data.get('email')
                    raw_password = form.cleaned_data.get('password1')
                    user.save()
                    login(request, incomplete_user, backend='django.contrib.auth.backends.ModelBackend')
                    return redirect('login')
        else:
            company_form = CompanyRegistrationForm()
            context['company_registration_form'] = company_form
        return render(request, 'core/register_company.html', context)


class LoginView(generic.ListView):
    def login(request):
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            queryset = User.objects.filter(email=email)
            if len(queryset) != 0:
                if queryset[0].is_active:
                    user = authenticate(email=email, password=password)
                    if user is not None:
                        login(request, user)
                        return redirect('index')
                    else:
                        request.messages.append({
                            "type": "warning",
                            "header": "Erreur liée au mot de passe",
                            "content": "Mot de passe incorrect"
                        })
                        return error(request)
                else:
                    print('inactive')
                    request.messages.append({
                        "type": "warning",
                        "header": "Erreur liée à votre compte",
                        "content": "Votre compte n'a pas encore été validée ou a été désactivé"
                    })
                    return error(request)

            else:
                request.messages.append({
                    "type": "warning",
                    "header": "Erreur liée à l'identifiant",
                    "content": "E-mail incorrect"
                })
                return error(request)
        else:
            return render(request, 'core/login.html')


class LogoutView(generic.ListView):
    def logout(request):
        logout(request)
        return HttpResponseRedirect('/')


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
        context = {}
        if request.POST:
            if 'event_creation' in request.POST:
                form = EventCreationForm(request.POST, request.FILES or None)
                if form.is_valid():
                    event = form.save(commit=False)
                    event.save()
                    return HttpResponseRedirect('/events/all_events')
                else:
                    context['event_creation_form'] = form
        else:
            event_form = EventCreationForm()
            context['event_creation_form'] = event_form
        return render(request, 'core/create_event.html', context)


class AllEventsView(generic.ListView):
    template_name = 'core/all_events.html'

    def all_events(request):
        """"
        Temporary solution while we do not construct the queryset method
        """
        events = Event.objects.all()
        return render(request, 'core/all_events.html', {'events': events})


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
        profiles = User.objects.all()
        return render(request, 'core/yearbook.html', {'profiles': profiles})

    def search_user(request):
        """"
        Temporary solution while we do not construct the queryset method
        """
        return render(request, 'core/search_user.html')


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

    def user_profile(request, user_id):
        user = User.objects.get(id=user_id)
        return render(request, 'core/user.html', {'user': user})


class UpdateUserView(generic.ListView):

    def update(request):
        return render(request, 'core/update.html')

    # def update_user(request):
    #     context = {}
    #     if request.POST:
    #         if 'user_update' in request.POST:
    #             form = UserUpdateForm(request.POST, request.FILES or None)
    #             if form.is_valid():
    #                 incomplete_user = form.save(commit=False)
    #                 incomplete_user.is_enterprise = False
    #                 incomplete_user.is_active = False
    #                 email = form.cleaned_data.get('email')
    #                 raw_password = form.cleaned_data.get('password1')
    #                 incomplete_user.save()
    #                 login(request, incomplete_user, backend='django.contrib.auth.backends.ModelBackend')
    #                 return redirect('login')
    #             else:
    #                 context['user_update_form'] = form
    #     else:
    #         user_form = UserRegistrationForm()
    #         context['user_update_form'] = user_form
    #     return render(request, 'core/update.html', context)


class CreateProgramView(generic.ListView):
    template_name = 'core/create_program.html'

    def create_program(request):
        """"
        Temporary solution while we do not construct the queryset method
        """
        return render(request, 'core/create_program.html')


class AllProgramsView(generic.ListView):
    template_name = 'core/all_programs.html'

    def all_programs(request):
        """"
        Temporary solution while we do not construct the queryset method
        """
        return render(request, 'core/all_programs.html')


class SearchProgramView(generic.ListView):
    template_name = 'core/search_program.html'

    def search_program(request):
        """"
        Temporary solution while we do not construct the queryset method
        """
        return render(request, 'core/search_program.html')


class SubscribeProgramsView(generic.ListView):
    template_name = 'core/subscribe_programs.html'

    def subscribe_programs(request):
        """"
        Temporary solution while we do not construct the queryset method
        """
        return render(request, 'core/subscribe_programs.html')
