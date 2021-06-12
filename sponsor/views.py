from django.shortcuts import render

# Create your views here.


def sponsorship_packages(request):
    """ This view will display all products """

    return render(request, 'sponsor/sponsor.html')