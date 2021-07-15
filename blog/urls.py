from django.urls import path
from . import views

urlpatterns = [
    path('', views.progress, name='progress'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit_post/<int:post_id>', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
]
