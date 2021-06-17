from django.shortcuts import render, redirect, reverse, HttpResponse

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


def update_basket(request, item_id):
    """View to handle the updating of a basket item's quantity"""

    quantity = int(request.POST.get('quantity'))

    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def delete_from_basket(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        basket = request.session.get('basket', {})
        basket.pop(item_id)

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)