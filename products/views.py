from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.

def all_products(request):
    """ This view will display all products """

    products = Product.objects.all()
    query = None
    category_friendly = 'All Categories'
    current_category = None
    current_sorting = 'Price Ascending'

    if request.GET:
        if 'product-filter' in request.GET:
            if request.GET['product-filter'] == 'all':
                category = None
            else:
                category = request.GET['product-filter']
                current_category = category
                products = products.filter(category__name=category)
                category_friendly = Category.objects.get(name=category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
            
            queries = Q(product_name__icontains=query) | Q(product_description__icontains=query)
            products = products.filter(queries)

        if 'product-sort' in request.GET:
            sortkey = request.GET['product-sort']
            print(sortkey)
            if sortkey == 'price_asc':
                products = products.order_by('price')
                current_sorting = 'Price Ascending'
            elif sortkey == 'price_desc':
                sort_direction = '-price'
                products = products.order_by(sort_direction)
                current_sorting = 'Price Descending'
            else:
                products = products.order_by('category')
                current_sorting = 'Category'

    context = {
        'products': products,
        'search_term': query,
        'category_friendly': category_friendly,
        'current_category': current_category,
        'current_sorting': current_sorting,

    }

    return render(request, 'products/products.html', context)