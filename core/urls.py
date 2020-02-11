from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.index, name='index'),
    path('events/', views.EventsView.events, name='events'),
    path('yearbook/', views.YearbookView.yearbook, name='yearbook'),
    path('programs/', views.ProgramsView.programs, name='programs'),
    path('user/', views.UserView.user, name='user'),
    path('create_event/', views.CreateEventView.create_event, name='create_event'),
    path('register/', views.RegisterView.register, name="register")

]

