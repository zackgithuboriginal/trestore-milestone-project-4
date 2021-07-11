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
    """View to display the user's profile page"""
    activeProfile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=activeProfile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your stored delivery details have been updated.')
        else:
            messages.error(request, 'Unable to update details. Ensure there is no errors in the form.')
    else:
        form = UserProfileForm(instance=activeProfile)
    orders = activeProfile.orders.all()
    template = "user_profiles/user_profile.html"
    trees_planted = int(float(activeProfile.tree_planting_contribution) / settings.TREE_PLANTING_BASE_COST)
    context = {
        'form': form,
        'orders': orders,
        'trees_planted': trees_planted,
        'profile': activeProfile,
        'profile_details': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/checkout_confirmation.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
