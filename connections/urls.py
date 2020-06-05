from django.urls import path

from .views import (
    ConnectionListView, 
    ConnectionDetailView, 
    ConnectionCreateView, 
    ConnectionUpdateView,
    ConnectionDeleteView
)

urlpatterns = [
    path('connection/<int:pk>/delete', ConnectionDeleteView.as_view(), name='connection_delete'),
    path('connection/<int:pk>/edit', ConnectionUpdateView.as_view(), name='connection_edit'),
    path('connection/new/', ConnectionCreateView.as_view(), name='connection_new'),
    path('connection/<int:pk>/', ConnectionDetailView.as_view(), name='connection_detail'),
    path('', ConnectionListView.as_view(), name='connection'),
]