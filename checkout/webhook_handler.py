from django.http import HttpResponse


class StripeWH_Handler:
    """Handles and processes Stripe webhook"""

    def __init__(self, request):
        self.request = request

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
        return HttpResponse(
            content=f'Stripe Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_failed(self, event):
        """
        Method handles a payment_intent_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'S tripe Webhook received: {event["type"]}',
            status=200)
