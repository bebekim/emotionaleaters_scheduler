from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Connection
# Create your views here.

class ConnectionListView(ListView):
    model = Connection
    template_name = 'connection.html'
    context_object_name = 'all_connections_list'

class ConnectionDetailView(DetailView):
    model = Connection
    template_name = 'connection_detail.html'
