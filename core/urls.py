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
    path('events/all_events/', views.AllEventsView.all_events, name='events/all_events'),
    path('events/search_events/', views.SearchEventsView.search_events, name='events/search_events'),
    path('events/subscribe_events/', views.SubscribeEventsView.subscribe_events, name='events/subscribe_events'),

]

