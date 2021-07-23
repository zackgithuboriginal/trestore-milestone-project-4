from django.shortcuts import render, redirect, reverse, HttpResponse, \
                            get_object_or_404
from django.contrib import messages
from products.models import Product


def view_basket(request):
    """
    A view that renders the basket display page
    """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """
    View to add a product to the request session basket object

    Accepts an item id as argument to access the corre
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))

    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request,
                         f'Quantity of {product.product_name} in'
                         ' basket has been updated.', extra_tags='checkout')
    else:
        basket[item_id] = quantity
        messages.success(request,
                         f'{product.product_name} has been addded'
                         ' to your basket!', extra_tags='checkout')

    request.session['basket'] = basket
    return redirect('products')


def update_basket(request, item_id):
    """
    View to handle the updating of a basket item's quantity
    """

    quantity = int(request.POST.get('quantity'))

    product = get_object_or_404(Product, pk=item_id)
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(request,
                         f'Quantity of {product.product_name} in basket'
                         ' has been updated.', extra_tags='checkout')
    else:
        basket.pop(item_id)
        messages.success(request,
                         f'{product.product_name} has been removed'
                         ' from your basket.', extra_tags='checkout')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def delete_from_basket(request, item_id):
    """
    Remove the item from the shopping bag
    """

    try:
        product = get_object_or_404(Product, pk=item_id)
        basket = request.session.get('basket', {})
        basket.pop(item_id)
        messages.success(request,
                         f'{product.product_name} has been removed'
                         ' from your basket.', extra_tags='checkout')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request,
                       f'Error removing {product.product_name}'
                       f' from basket. Error message: {e}')

        return HttpResponse(status=500)
