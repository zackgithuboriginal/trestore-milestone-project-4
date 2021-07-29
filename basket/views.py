from django.shortcuts import render, redirect, reverse, HttpResponse, \
                            get_object_or_404
from django.contrib import messages
from products.models import Product


def view_basket(request):
    """
    A view that renders the basket display page
    """

    return render(request, 'basket/basket.html')


def add_to_basket(request,
                  item_id, location,
                  sort='price_asc',
                  filter='all',
                  search=None):
    """
    View to add a product to the request session basket object

    Parameters accepted:
    item id: to provide access the correct product

    location: to allow for redirecting to the correct page

    sort, filter, search: store search parameters to allow for the store page
    to be rendered with the correct search results when the page is reloaded
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))

    basket = request.session.get('basket', {})

    """
    If the product is already in basket, quantity will be updated
    else new item will be added to basket
    """
    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        if product.category.name != 'sponsorship' :
            messages.success(request,
                            f'Quantity of {product.product_name} in your'
                            ' basket has been updated.', extra_tags='checkout')
        else:
            messages.success(request,
                            f'Quantity of the {product.product_name} package'
                            ' in your basket has been updated.', extra_tags='checkout')

    else:
        basket[item_id] = quantity
        if product.category.name != 'sponsorship' :
            messages.success(request,
                            f'{product.product_name} has been added'
                            ' to your basket!', extra_tags='checkout')
        else:
            messages.success(request,
                            f'Package for {product.product_name} has been added'
                            ' to your basket!', extra_tags='checkout')

    request.session['basket'] = basket

    """
    Logic loop to redirect user to the origin page of the
    add to basket request

    if request origin is the products store, products filter,
    sort and search parameters will be added to the redirect template
    """
    if location == 'product_details':
        return redirect(location, product.id)
    elif location == 'products':
        if filter != 'all':
            filter_arg = f"product-filter={filter}"
        else:
            filter_arg = "all"
        if sort != 'price_asc':
            sort_arg = f"product-sort={sort}"
        else:
            sort_arg = "product-sort=price_asc"
        if search is not None:
            search_arg = f"q={search}"
            return redirect(f"{reverse(location)}"
                            f"?{filter_arg}&{sort_arg}&{search_arg}")
        else:
            return redirect(f"{reverse(location)}?{filter_arg}&{sort_arg}")
    else:
        return redirect(location)


def update_basket(request, item_id):
    """
    View to handle the updating of a basket item's quantity
    """

    quantity = int(request.POST.get('quantity'))

    product = get_object_or_404(Product, pk=item_id)
    basket = request.session.get('basket', {})

    """
    If new quantity of product is greater than one basket updated
    and user sent feedback message
    else product removed from basket and user sent feedback
    """
    if quantity > 0:
        basket[item_id] = quantity
        if product.category.name != 'sponsorship' :
            messages.success(request,
                            f'Quantity of {product.product_name} in your'
                            ' basket has been updated.', extra_tags='checkout')
        else:
            messages.success(request,
                            f'Quantity of the {product.product_name} package'
                            ' in your basket has been updated.', extra_tags='checkout')
    else:
        basket.pop(item_id)
        messages.success(request,
                         f'{product.product_name} has been removed'
                         ' from your basket.', extra_tags='checkout')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def delete_from_basket(request, item_id):
    """
    View to handle removing the item from the shopping bag
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
