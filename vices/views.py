from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Vice
# Create your views here.


class ViceListView(LoginRequiredMixin, ListView):
    model = Vice
    context_object_name = 'all_vices_list'
    template_name = 'vice_list.html'
    login_url = 'account_login'

class ViceCreateView(LoginRequiredMixin, CreateView):
    model = Vice
    template_name = 'vice_new.html'
    fields = ('location', 'occasion', 'consumption', 'consumption_date')
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ViceDetailView(LoginRequiredMixin, DetailView):
    model = Vice
    template_name = 'vice_detail.html'
    fields = ['location', 'occasion', 'connection', 'involved_one', 'consumption', 'consumption_date']
    login_url = 'account_login'

class ViceUpdateView(UpdateView):
    model = Vice
    template_name = 'vice_edit.html'
    fields = ['location', 'occasion', 'connection', 'involved_one', 'consumption', 'consumption_date']


class ViceDeleteView(DeleteView):
    model = Vice
    template_name = 'vice_delete.html'
    success_url = reverse_lazy('vice_list')
