from django.urls import path

from .views import (
    ActionListView, 
    # ActionDetailView, 
    # ActionCreateView, 
    # ActionUpdateView,
    # ActionDeleteView
)

urlpatterns = [
    # path('<int:pk>/delete', ActionDeleteView.as_view(), name='action_delete'),
    # path('<int:pk>/edit', ActionUpdateView.as_view(), name='action_edit'),
    # path('new/', ActionCreateView.as_view(), name='action_new'),
    # path('<int:pk>/', ActionDetailView.as_view(), name='action_detail'),
    path('', ActionListView.as_view(), name='action'),
]