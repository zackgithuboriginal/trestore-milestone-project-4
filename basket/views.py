from django.shortcuts import render

# Create your views here.

def view_basket(request):
    """A view thata renders the basket display page """
    
    return render(request, 'basket/basket.html')