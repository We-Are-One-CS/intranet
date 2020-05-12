import datetime

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views import generic

from .forms import EventCreationForm, UserUpdateForm
from .forms import UserRegistrationForm, CompanyRegistrationForm
from .models import User, Event
from django.db.models import Q
import xlwt


def error(request, message="Bienvenue sur la page d'affichage d'erreurs !"):
    # This special view is called everytime there is an error to display it into the browser
    return render(request, 'wao/error.html', {'messages': request.messages, })


class IndexView(generic.ListView):
    template_name = 'wao/index.html'

    def index(request):
        """"
        Temporary solution while we do not construct the queryset method
        """

        # The next 5 events from today on
        events = Event.objects.filter(begin_date__gt=datetime.date.today()).order_by("begin_date")[:5]

        return render(request, 'wao/index.html', context={'events': events})


class RegisterView:
    def register(request):
        return render(request, 'wao/register.html')

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
        return render(request, 'wao/register_user.html', context)

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
        return render(request, 'wao/register_company.html', context)


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
            return render(request, 'wao/login.html')


class LogoutView(generic.ListView):
    def logout(request):
        logout(request)
        return HttpResponseRedirect('/')


class EventsView(generic.ListView):
    template_name = 'wao/events.html'

    def events(request):
        """"
        Temporary solution while we do not construct the queryset method
        """
        return render(request, 'wao/events.html')


class CreateEventView(generic.ListView):
    template_name = 'wao/create_event.html'

    def create_event(request):
        context = {}
        if request.POST:
            if 'event_creation' in request.POST:
                form = EventCreationForm(request.POST, request.FILES or None)
                if form.is_valid():
                    event = form.save(commit=False)
                    event.owner = request.user
                    event.save()
                    return HttpResponseRedirect('/events/all_events')
                else:
                    context['event_creation_form'] = form
        else:
            event_form = EventCreationForm()
            context['event_creation_form'] = event_form
        return render(request, 'wao/create_event.html', context)


class AllEventsView(generic.ListView):
    template_name = 'wao/all_events.html'

    def all_events(request):
        """"
        Temporary solution while we do not construct the queryset method
        """
        events = Event.objects.all()
        return render(request, 'wao/all_events.html', {'events': events})


class EventInfoView(generic.ListView):
    template_name = 'wao/event_info.html'

    def event_info(request, event_id):
        """"
        Temporary solution while we do not construct the queryset method
        """
        event = Event.objects.get(id=event_id)
        
        total = len(event.participants.all()) + event.capacity
        show_participate = True

        for participant in event.participants.all():
            if request.user == participant:
                show_participate = False

        return render(request, 'wao/event_info.html', {'event': event, 'show_participate': show_participate, 'total':total})


class SearchEventsView(generic.ListView):
    template_name = 'wao/search_events.html'

    def search_events(request):
        """"
        Temporary solution while we do not construct the queryset method
        """
        query = request.GET.get('q')
        searched_events = Event.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(type__icontains=query)
        )

        return render(request, 'wao/all_events.html', {'events': searched_events})


class SubscribeEventsView(generic.ListView):
    template_name = 'wao/event_info.html'

    def subscribe_events(request, event_id, user_id):
        """"
        Temporary solution while we do not construct the queryset method
        """
        
        event = Event.objects.get(id=event_id)
        user = User.objects.get(id=user_id)
        event.participants.add(user)
        event.capacity = event.capacity -1
        event.save()

        total = len(event.participants.all()) + event.capacity
        show_participate = True
        
        for participant in event.participants.all():
            if request.user == participant:
                show_participate = False


        return HttpResponseRedirect('/events/event_info/'+ str(event.id))

    def unsubscribe_events(request, event_id, user_id):
        """"
        Temporary solution while we do not construct the queryset method
        """
        
        event = Event.objects.get(id=event_id)
        user = User.objects.get(id=user_id)
        event.participants.remove(user)
        event.capacity = event.capacity +1
        event.save()

        total = len(event.participants.all()) + event.capacity
        show_participate = True
        
        for participant in event.participants.all():
            if request.user == participant:
                show_participate = False


        return HttpResponseRedirect('/events/event_info/'+ str(event.id))
    
    def get_participants(request, event_id):
        
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = "attachment; filename=participants.xls"

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Participants')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Prénom', 'Nom', 'Email', 'Téléphone', ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        event = Event.objects.get(id=event_id)
        rows = event.participants.all().values_list('first_name', 'last_name', 'email', 'telephone')
        
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        
        wb.save(response)
        return response





class YearbookView(generic.ListView):
    template_name = 'wao/yearbook.html'

    def yearbook(request):
        """"
        Temporary solution while we do not construct the queryset method
        """
        profiles = User.objects.all()
        return render(request, 'wao/yearbook.html', {'profiles': profiles})

    def search_user(request):
        """"
        Temporary solution while we do not construct the queryset method
        """
        query = request.GET.get('q')
        searched_profiles = User.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )

        return render(request, 'wao/yearbook.html', {'profiles': searched_profiles})


class ProgramsView(generic.ListView):
    template_name = 'wao/programs.html'

    def programs(request):
        """"
        Temporary solution while we do not construct the queryset method
        """
        return render(request, 'wao/programs.html')


class UserView(generic.ListView):

    def user(request):
        """"
        Temporary solution while we do not construct the queryset method
        """
        return render(request, 'wao/user.html')

    def user_profile(request, user_id):
        user = User.objects.get(id=user_id)
        return render(request, 'wao/user.html', {'user': user})


class UpdateUserView(generic.ListView):

    # def update(request):
    #     return render(request, 'wao/update.html')

    def update(request):
        context = {}
        if request.POST:
            if 'user_update' in request.POST:
                form = UserUpdateForm(request.POST, request.FILES or None)
                if form.is_valid():
                    incomplete_user = form.save(commit=False)
                    incomplete_user.save()
                    return redirect('index')
                else:
                    context['user_update_form'] = form
        else:
            user_form = UserUpdateForm()
            context['user_update_form'] = user_form
        return render(request, 'wao/update.html', context)


class ChangeUserPasswordView(generic.ListView):

    def change_password(request):
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return redirect('change_password')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'wao/change_password.html', {
            'form': form
        })


class CreateProgramView(generic.ListView):
    template_name = 'wao/create_program.html'

    def create_program(request):
        """"
        Temporary solution while we do not construct the queryset method
        """
        return render(request, 'wao/create_program.html')


class AllProgramsView(generic.ListView):
    template_name = 'wao/all_programs.html'

    def all_programs(request):
        """"
        Temporary solution while we do not construct the queryset method
        """
        return render(request, 'wao/all_programs.html')


class SearchProgramView(generic.ListView):
    template_name = 'wao/search_program.html'

    def search_program(request):
        """"
        Temporary solution while we do not construct the queryset method
        """
        return render(request, 'wao/search_program.html')


class SubscribeProgramsView(generic.ListView):
    template_name = 'wao/subscribe_programs.html'

    def subscribe_programs(request):
        """"
        Temporary solution while we do not construct the queryset method
        """
        return render(request, 'wao/subscribe_programs.html')


class ModerationView(generic.ListView):

    def moderate_user(request):
        """"
        Temporary solution while we do not construct the queryset method
        """
        return render(request, 'wao/moderate_user.html')

    def moderate_event(request):
        """"
        Temporary solution while we do not construct the queryset method
        """
        return render(request, 'wao/moderate_event.html')