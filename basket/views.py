from django.shortcuts import render, redirect

# Create your views here.

def view_basket(request):
    """A view thata renders the basket display page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """Add a specific product to basket"""

    quantity = int(request.POST.get('quantity'))

    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect('products')
