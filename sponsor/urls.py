from django.urls import path
from . import views

urlpatterns = [
    path('', views.sponsorship_packages, name='sponsor')
]
