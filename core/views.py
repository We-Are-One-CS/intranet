from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


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


class EventsView(generic.ListView):
    template_name = 'core/events.html'

    def events(request):
        """"
        Temporary solution while we do not construct the queryset method
        """
        return render(request, 'core/events.html')


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

