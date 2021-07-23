from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from django.contrib import messages


def basket_contents(request):
    """
    Basket content context containing information regarding
    contents of basket and total price of products
    """
    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})
    for item_id, quantity in basket.items():
        try:
            product = get_object_or_404(Product, pk=item_id)
            total += quantity * product.price
            product_count += quantity
            basket_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
            })
        except Exception:
            messages.error(request,
                           "Unfortunately a product in your basket is no"
                           " longer available.")
            basket.pop(item_id, quantity)
            request.session['basket'] = basket
            break

    delivery_cost = total * Decimal(settings.DELIVERY_PERCENTAGE / 100)

    grand_total = delivery_cost + total

    tree_planting_contribution = total * Decimal(
                                         settings.TREE_PLANTING_PERCENTAGE /
                                         100)

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery_cost': delivery_cost,
        'tree_planting_contribution': tree_planting_contribution,
        'tree_planting_percentage': settings.TREE_PLANTING_PERCENTAGE,
        'grand_total': grand_total,
    }

    return context
