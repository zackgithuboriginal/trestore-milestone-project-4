from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.

def all_products(request):
    """ This view will display all products """

    products = Product.objects.all()
    query = None
    category = None

    if request.GET:
        if 'product-filter' in request.GET:
            if request.GET['product-filter'] == 'all':
                pass
            else:
                category = request.GET['product-filter']
                products = products.filter(category__name=category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
            
            queries = Q(product_name__icontains=query) | Q(product_description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_category': category,
    }

    return render(request, 'products/products.html', context)