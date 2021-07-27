from django.shortcuts import render, reverse, redirect, \
    get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from basket.contexts import basket_contents
from products.models import Product
from user_profiles.models import UserProfile
from user_profiles.forms import UserProfileForm
from .models import OrderLineItem, Order

import stripe
import json
# Create your views here.


@require_POST
def cache_checkout_data(request):
    """
    View handles caching all of the order details

    passes the basket details,
    the binary store details option
    and the user's username into the payment intent
    to be received by the webhook handler
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'store_details': request.POST.get('store_details'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    View either renders the checkout page, or if it receives a POST request,
    handles the submission of the order object to stripe
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        """
        If checkout form submitted, request.form data is accesssed
        and input into the OrderForm
        """
        basket = request.session.get('basket', {})
        form_data = {
                    'full_name': request.POST['full_name'],
                    'email': request.POST['email'],
                    'street_address1': request.POST['street_address1'],
                    'street_address2': request.POST['street_address2'],
                    'town_or_city': request.POST['town_or_city'],
                    'postcode': request.POST['postcode'],
                    'county': request.POST['county'],
                    'country': request.POST['country'],
                }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            """
            If OrderForm is valid with no errors the order object is created,
            the order then has the checkout basket data and stripe_pid
            attached to it, and is saved

            then the orderlineitem objects are created from the basket
            and are saved
            """
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.basket = json.dumps(basket)
            order.save()
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
                        "Unfortunately one of the"
                        " items in your basket is unavailable!")
                    )
                    order.delete()
                    return redirect(reverse('view_basket'))

            request.session['store_details'] = 'store_details' in request.POST
            return redirect(reverse(
                            'checkout_confirmation',
                            args=[order.order_number]))
    else:
        """
        If request does not contains POST request initialise
        the checkout form, if the user is authenticated
        and has dlivery details stored,
        those details will be input into form and submitted to rendered page
        in context
        """
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, "You need to have"
                           " items in your basket to checkout.")
            return redirect(reverse('products'))

        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.default_full_name,
                    'email': profile.user.email,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'town_or_city': profile.default_town_or_city,
                    'postcode': profile.default_postcode,
                    'county': profile.default_county,
                    'country': profile.default_country,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
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

    if user is authenticated checks if they
    have request to store their details
    if so: the profile is updated with those details

    if basket is still in session it is deleted
    as it has already been checked out

    renders the checkout confirmation page with order details
    """
    store_details = request.session.get('store_details')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # The order is saved to the user's profile
        order.user_profile = profile
        order.save()

        # The user's details are stored to their profile if check box checked
        if store_details:
            profile_data = {
                'default_full_name': order.full_name,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order confirmed! \
                                Order number: {order_number} \
                                You will receive a confirmation \
                                email with details.')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_confirmation.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
