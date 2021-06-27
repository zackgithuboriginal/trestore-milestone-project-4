from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from basket.contexts import basket_contents
from products.models import Product
from .models import OrderLineItem, Order

import stripe
# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})
        form_data = {
                    'full_name': request.POST['full_name'],
                    'email': request.POST['email'],
                    'phone_number': request.POST['phone_number'],
                    'country': request.POST['country'],
                    'postcode': request.POST['postcode'],
                    'town_or_city': request.POST['town_or_city'],
                    'street_address1': request.POST['street_address1'],
                    'street_address2': request.POST['street_address2'],
                    'county': request.POST['county'],
                }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in basket.items():
                try:
                    product = get_object_or_404(Product, pk=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                        )
                    order_line_item.save()

                except Product.DoesNotExist:
                    messages.error(request, (
                        "Unfortunately one of the items in your basket is unavailable!")
                    )
                    order.delete()
                    return redirect(reverse('view_basket'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_confirmation', args=[order.order_number]))
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, "You need to have items in your basket to checkout.")
            return redirect(reverse('products'))

        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_confirmation(request, order_number):
    """
    This view handles a successful checkout request
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order confirmed! \
                                Order number: {order_number} \
                                You will receive a confirmation email with details.')
    
    if 'basket' in request.session:
        del request.session['basket']
    
    template = 'checkout/checkout_confirmation.html'
    context = { 
        'order': order,
    }

    return render(request, template, context)