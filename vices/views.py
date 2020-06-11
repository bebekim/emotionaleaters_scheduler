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

