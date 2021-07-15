from django.urls import path
from . import views

urlpatterns = [
    path('', views.progress, name='progress'),
    path('add_post/', views.add_post, name='add_post'),
]
