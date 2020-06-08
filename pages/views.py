from django.views.generic import TemplateView, ListView
from connections.models import Connection

class AboutPageView(TemplateView):
    template_name = 'about.html'

class HomePageView(ListView):
    model = Connection
    template_name = 'home.html'
    context_object_name = 'all_connections_list'