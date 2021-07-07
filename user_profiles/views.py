from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


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
        'profile_details': True,
    }

    return render(request, template, context)
