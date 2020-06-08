from django.urls import path

from .views import (
    ConnectionListView, 
    ConnectionDetailView, 
    ConnectionCreateView, 
    ConnectionUpdateView,
    ConnectionDeleteView
)

urlpatterns = [
    path('<int:pk>/delete', ConnectionDeleteView.as_view(), name='connection_delete'),
    path('<int:pk>/edit', ConnectionUpdateView.as_view(), name='connection_edit'),
    path('new/', ConnectionCreateView.as_view(), name='connection_new'),
    path('<int:pk>/', ConnectionDetailView.as_view(), name='connection_detail'),
    path('', ConnectionListView.as_view(), name='connection'),
]