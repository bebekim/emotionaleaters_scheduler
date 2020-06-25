from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Action
# Create your views here.

class ActionListView(LoginRequiredMixin, ListView):
    model = Action
    context_object_name = 'all_actions_list'
    template_name = 'action.html'
    login_url = 'account_login'

class ActionCreateView(LoginRequiredMixin, CreateView):
    model = Action
    template_name = 'action_new.html'
    fields = ('name', 'description')
    login_url = 'account_login'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ActionDetailView(LoginRequiredMixin, DetailView):
    model = Action
    template_name = 'action_detail.html'
    fields = ['name', 'author', 'created_date', 'description']
    login_url = 'account_login'


class ActionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Action
    fields = ['name', 'description']
    template_name = 'action_edit.html'
    login_url = 'account_login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ActionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Action
    template_name = 'action_delete.html'
    success_url = reverse_lazy('action')
    login_url = 'account_login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user