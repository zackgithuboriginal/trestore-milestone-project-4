from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('sponsorship_packages/', views.sponsorship_packages, name='sponsorship_packages'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('product_details/<int:product_id>/', views.product_details, name='product_details'),
]
