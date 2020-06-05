from django.urls import path

from .views import ConnectionListView, ConnectionDetailView

urlpatterns = [
    path('connection/<int:pk>/', ConnectionDetailView.as_view(), name='connection_detail'),
    path('', ConnectionListView.as_view(), name='connection'),
]