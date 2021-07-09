from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


# Create your views here.
def user_profile(request):
    """View to display the user's profile page"""
    activeProfile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=activeProfile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your stored delivery details have been updated.')
    form = UserProfileForm(instance=activeProfile)
    orders = activeProfile.orders.all()
    template = "user_profiles/user_profile.html"
    context = {
        'form': form,
        'orders': orders,
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
