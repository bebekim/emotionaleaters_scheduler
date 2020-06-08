from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Connection
# Create your views here.

class ConnectionListView(LoginRequiredMixin, ListView):
    model = Connection
    context_object_name = 'all_connections_list'
    template_name = 'connection.html'
    login_url = 'account_login'

class ConnectionDetailView(DetailView):
    model = Connection
    template_name = 'connection_detail.html'
    fields = ['emotion', 'author', 'reason']
    login_url = 'account_login'

class ConnectionCreateView(LoginRequiredMixin, CreateView):
    model = Connection
    template_name = 'connection_new.html'
    fields = ('emotion', 'reason')
    login_url = '/login/'
#    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ConnectionUpdateView(UpdateView):
    model = Connection
    template_name = 'connection_edit.html'
    fields = ['emotion', 'reason']

class ConnectionDeleteView(DeleteView):
    model = Connection
    template_name = 'connection_delete.html'
    success_url = reverse_lazy('connection')
