from django.urls import path

from .views import (
    ConnectionListView, 
    ConnectionDetailView, 
    ConnectionCreateView, 
    ConnectionUpdateView,
    ConnectionDeleteView
)

urlpatterns = [
    path('<uuid:pk>/delete', ConnectionDeleteView.as_view(), name='connection_delete'),
    path('<uuid:pk>/edit', ConnectionUpdateView.as_view(), name='connection_edit'),
    path('new/', ConnectionCreateView.as_view(), name='connection_new'),
    path('<uuid:pk>/', ConnectionDetailView.as_view(), name='connection_detail'),
    path('', ConnectionListView.as_view(), name='connection'),
]