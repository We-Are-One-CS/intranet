from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.index, name='index'),
    path('events/', views.EventsView.events, name='events'),
    path('yearbook/', views.YearbookView.yearbook, name='yearbook'),
    path('programs/', views.ProgramsView.programs, name='programs'),
    path('user/', views.UserView.user, name='user'),
    path('events/create_event/', views.CreateEventView.create_event, name='events/create_event'),
    path('register/', views.RegisterView.register, name="register"),
    path('login/', views.LoginView.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('events/all_events/', views.AllEventsView.all_events, name='events/all_events'),
    path('events/search_events/', views.SearchEventsView.search_events, name='events/search_events'),
    path('events/subscribe_events/', views.SubscribeEventsView.subscribe_events, name='events/subscribe_events'),
    path('error', views.error, name='error'),

    path('programs/', views.ProgramsView.programs, name='programs'),
    path('programs/create_program/', views.CreateProgramView.create_program, name='programs/create_program'),
    path('programs/all_programs/', views.AllProgramsView.all_programs, name='programs/all_programs'),
    path('programs/search_programs/', views.SearchProgramView.search_program, name='programs/search_program'),
    path('programs/subscribe_programs/', views.SubscribeProgramsView.subscribe_programs,
         name='programs/subscribe_programs'),

    path('yearbook/', views.YearbookView.yearbook, name='yearbook'),
]
