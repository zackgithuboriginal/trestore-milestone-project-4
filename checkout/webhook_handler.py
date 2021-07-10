from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from decimal import Decimal


from products.models import Product
from user_profiles.models import UserProfile
from .models import Order, OrderLineItem
import time

import json
class StripeWH_Handler:
    """Handles and processes Stripe webhook"""

    def __init__(self, request):
        self.request = request
    
    def _send_confirmation_email(self, order):
        """Method to send a confirmation email when an order is placed"""
        target_email = order.email
        email_subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order}
        )
        email_body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_EMAIL}
        )
        send_mail(
            email_subject,
            email_body,
            settings.DEFAULT_EMAIL,
            [target_email],
        )

    def handle_event(self, event):
        """
        Method handles the webhook event
        """
        return HttpResponse(
            content=f'Unhandled Stripe Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Method handles a payment_intent_succeeded webhook from Stripe
        """
       
        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        store_details = intent.metadata.store_details

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Removes fields that contain only empty strings
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update user details from payment itent
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if store_details:
                profile.default_full_name = shipping_details.name
                profile.default_street_address1 = shipping_details.address.line1
                profile.default_street_address2 = shipping_details.address.line2
                profile.default_town_or_city = shipping_details.address.city
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_county = shipping_details.address.state
                profile.default_country = shipping_details.address.country
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    basket=basket,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            if username != 'AnonymousUser':
                profile = UserProfile.objects.get(user__username=username)
                profile.tree_planting_contribution = profile.tree_planting_contribution+order.order_total*Decimal(settings.TREE_PLANTING_PERCENTAGE / 100)
                profile.save()
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    basket=basket,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(basket).items():
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            profile.tree_planting_contribution = profile.tree_planting_contribution+order.order_total*Decimal(settings.TREE_PLANTING_PERCENTAGE / 100)
            profile.save()
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_failed(self, event):
        """
        Method handles a payment_intent_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'S tripe Webhook received: {event["type"]}',
            status=200)
