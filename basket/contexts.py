from decimal import Decimal
from django.conf import settings

def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0

    delivery_cost = total * Decimal(settings.DELIVERY_PERCENTAGE)

    grand_total = delivery_cost + total

    tree_planting_contribution = total * Decimal(settings.TREE_PLANTING_PERCENTAGE)

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery_cost': delivery_cost,
        'tree_planting_contribution': tree_planting_contribution,
        'tree_planting_percentage': settings.TREE_PLANTING_PERCENTAGE,
    }


    return context