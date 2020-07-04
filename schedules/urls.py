from django.urls import path

from .views import (
    SchedulerView, 
    # ScheduleDetailView, 
    # ScheduleCreateView, 
    # ScheduleUpdateView,
    # ScheduleDeleteView,
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
    path('act/', ActListView.as_view(), name='act'),

    # path('scheduler/<uuid:pk>/delete', ScheduleDeleteView.as_view(), name='connection_delete'),
    # path('scheduler/<uuid:pk>/edit', ScheduleUpdateView.as_view(), name='connection_edit'),
    # path('scheduler/new/', ScheduleCreateView.as_view(), name='connection_new'),
    # path('scheduler/<uuid:pk>/', ScheduleDetailView.as_view(), name='connection_detail'),
    path('scheduler', SchedulerView.as_view(), name='scheduler'),

]
