from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Conditioning
# Create your views here.

class ConditioningListView(LoginRequiredMixin, ListView):
    model = Conditioning
    # context_object_name = 'all_conditionings_list'
    template_name = 'conditioning.html'
    login_url = 'account_login'

# class ConditioningCreateView(LoginRequiredMixin, CreateView):
#     model = Conditioning
#     template_name = 'connection_new.html'
#     fields = ('emotion', 'reason')
#     login_url = 'account_login'
# #    redirect_field_name = 'redirect_to'

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

# class ConditioningDetailView(LoginRequiredMixin, DetailView):
#     model = Conditioning
#     template_name = 'connection_detail.html'
#     fields = ['emotion', 'author', 'reason']
#     login_url = 'account_login'


# class ConditioningUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Conditioning
#     fields = ['emotion', 'reason']
#     template_name = 'connection_edit.html'
#     login_url = 'account_login'

#     def test_func(self):
#         obj = self.get_object()
#         return obj.author == self.request.user

# class ConditioningDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Conditioning
#     template_name = 'connection_delete.html'
#     success_url = reverse_lazy('connection')
#     login_url = 'account_login'

#     def test_func(self):
#         obj = self.get_object()
#         return obj.author == self.request.user

    
