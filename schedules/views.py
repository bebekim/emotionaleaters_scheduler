from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Schedule
# Create your views here.

class ScheduleListView(LoginRequiredMixin, ListView):
    model = Schedule
    # context_object_name = 'all_conditionings_list'
    template_name = 'schedule.html'
    login_url = 'account_login'

# class ScheduleCreateView(LoginRequiredMixin, CreateView):
#     model = Schedule
#     template_name = 'connection_new.html'
#     fields = ('emotion', 'reason')
#     login_url = 'account_login'
# #    redirect_field_name = 'redirect_to'

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

# class ScheduleDetailView(LoginRequiredMixin, DetailView):
#     model = Schedule
#     template_name = 'connection_detail.html'
#     fields = ['emotion', 'author', 'reason']
#     login_url = 'account_login'


# class ScheduleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Schedule
#     fields = ['emotion', 'reason']
#     template_name = 'connection_edit.html'
#     login_url = 'account_login'

#     def test_func(self):
#         obj = self.get_object()
#         return obj.author == self.request.user

# class ScheduleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Schedule
#     template_name = 'connection_delete.html'
#     success_url = reverse_lazy('connection')
#     login_url = 'account_login'

#     def test_func(self):
#         obj = self.get_object()
#         return obj.author == self.request.user

    