from django.urls import path

from .views import (
    ScheduleListView, 
    # ScheduleDetailView, 
    # ScheduleCreateView, 
    # ScheduleUpdateView,
    # ScheduleDeleteView
)

urlpatterns = [
    # path('<uuid:pk>/delete', ScheduleDeleteView.as_view(), name='connection_delete'),
    # path('<uuid:pk>/edit', ScheduleUpdateView.as_view(), name='connection_edit'),
    # path('new/', ScheduleCreateView.as_view(), name='connection_new'),
    # path('<uuid:pk>/', ScheduleDetailView.as_view(), name='connection_detail'),
    path('', ScheduleListView.as_view(), name='schedule'),
]
