from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_confirmation/<order_number>', views.checkout_confirmation, name='checkout_confirmation'),
    path('wh/', webhook, name='webhook'),
]
