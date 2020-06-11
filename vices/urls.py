from django.urls import path

from .views import (
    ViceListView, 
    # ViceDetailView, 
    # ViceCreateView, 
    # ViceUpdateView,
    # ViceDeleteView
)

urlpatterns = [
    # path('<int:pk>/delete', ViceDeleteView.as_view(), name='vice_delete'),
    # path('<int:pk>/edit', ViceUpdateView.as_view(), name='vice_edit'),
    # path('new/', ViceCreateView.as_view(), name='vice_new'),
    # path('<int:pk>/', ViceDetailView.as_view(), name='vice_detail'),
    path('', ViceListView.as_view(), name='vice_list'),
]