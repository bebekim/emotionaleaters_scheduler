from django.urls import path

from .views import (
    ConditioningListView, 
    # ConditioningDetailView, 
    # ConditioningCreateView, 
    # ConditioningUpdateView,
    # ConditioningDeleteView
)

urlpatterns = [
    # path('<uuid:pk>/delete', ConditioningDeleteView.as_view(), name='connection_delete'),
    # path('<uuid:pk>/edit', ConditioningUpdateView.as_view(), name='connection_edit'),
    # path('new/', ConditioningCreateView.as_view(), name='connection_new'),
    # path('<uuid:pk>/', ConditioningDetailView.as_view(), name='connection_detail'),
    path('', ConditioningListView.as_view(), name='conditioning'),
]
