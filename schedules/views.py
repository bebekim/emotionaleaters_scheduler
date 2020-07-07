from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Act, ActionCategory, Schedule, ScheduleAct
# Create your views here.

class SchedulerView(LoginRequiredMixin, ListView):
    model = Schedule
    # context_object_name = 'all_conditionings_list'
    template_name = 'scheduler.html'
    login_url = 'account_login'

# class UserSchedulerView(LoginRequiredMixin, ListView):
#     model = Schedule
#     context_object_name = 'user_scheduler'
#     login_url = 'account_login'

#     def get_queryset(self):
#         return Schedule.objects.filter(user=self.request.user)

class ActListView(LoginRequiredMixin, ListView):
    model = Act
    context_object_name = 'user_acts_list'
#    context_object_name = 'all_acts_list'
    template_name = 'act.html'
    login_url = 'account_login'

class ActCreateView(LoginRequiredMixin, CreateView):
    model = Act
    template_name = 'act_new.html'
    fields = ['title', 'category', 'description', 'tags', 'builds_confidence', 'image']
    login_url = 'account_login'
#    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ActDetailView(LoginRequiredMixin, DetailView):
    model = Act
    template_name = 'act_detail.html'
    fields = ['title', 'category', 'description', 'tags', 'builds_confidence']
    login_url = 'account_login'


# class ActUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Act
#     fields = ['emotion', 'reason']
#     template_name = 'act_edit.html'
#     login_url = 'account_login'

#     def test_func(self):
#         obj = self.get_object()
#         return obj.author == self.request.user

# class ActDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Act
#     template_name = 'act_delete.html'
#     success_url = reverse_lazy('connection')
#     login_url = 'account_login'

#     def test_func(self):
#         obj = self.get_object()
#         return obj.author == self.request.user

    
