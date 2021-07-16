from django.urls import path
from . import views

urlpatterns = [
    path('', views.progress, name='progress'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit_post/<int:post_id>', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
    path('add_comment/<int:post_id>', views.add_comment, name='add_comment'),
    path('delete_comment/<int:comment_id>', views.delete_comment, name='delete_comment'),
]
