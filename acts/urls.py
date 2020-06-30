from django.urls import path

from .views import (
    ActListView, 
    # ActDetailView, 
    # ActCreateView, 
    # ActUpdateView,
    # ActDeleteView
)

urlpatterns = [
    # path('<uuid:pk>/delete', ActDeleteView.as_view(), name='connection_delete'),
    # path('<uuid:pk>/edit', ActUpdateView.as_view(), name='connection_edit'),
    # path('new/', ActCreateView.as_view(), name='connection_new'),
    # path('<uuid:pk>/', ActDetailView.as_view(), name='connection_detail'),
    path('', ActListView.as_view(), name='act'),
]
