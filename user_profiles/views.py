from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


# Create your views here.
@login_required
def user_profile(request):
    """
    View to either display the userprofile template or
    if there is a post request to update the delivery details
    attached to the userprofile model
    """
    activeProfile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=activeProfile)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Your stored delivery details have been updated.')
        else:
            messages.error(request,
                           'Unable to update details.'
                           ' Ensure there is no errors in the form.')
    else:
        form = UserProfileForm(instance=activeProfile)
    orders = activeProfile.orders.all()
    template = "user_profiles/user_profile.html"
    """
    Trees_planted is a profile variable that tracks the number
    of trees planted due to the contributions
    of a user through sales and is passed to the template
    throught he context object
    """
    trees_planted = int(
                        float(
                              activeProfile.tree_planting_contribution) / (
                              settings.TREE_PLANTING_BASE_COST))
    context = {
        'form': form,
        'orders': orders,
        'trees_planted': trees_planted,
        'profile': activeProfile,
        'profile_details': True,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """
    View to render the order details page for a specific order

    Accepts the request object and order number in order to
    access the correct order object and then passes the order
    to the template in a context object.

    Also passes a from profile variable to prevent the creation
    of an order successful feedback message
    """
    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/checkout_confirmation.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
