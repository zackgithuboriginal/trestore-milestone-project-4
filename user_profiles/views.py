from django.shortcuts import render

# Create your views here.
def user_profile(request):
    """View to display the user's profile page"""
    template = "user_profiles/user_profile.html"
    context = {}

    return render(request, template, context)
