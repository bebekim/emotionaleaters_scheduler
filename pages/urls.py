from django.urls import path

from .views import (
    AboutPageView,
    HomePageView
)

urlpatterns = [
    path('',  HomePageView.as_view(), name='connection'),
    path('about/', AboutPageView.as_view(), name='about'),
]