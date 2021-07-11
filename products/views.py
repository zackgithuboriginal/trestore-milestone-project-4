from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from .forms import AddProductForm

# Create your views here.

def all_products(request):
    """ This view will display all products """

    products = Product.objects.all()
    sortkey = None
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
            if sortkey == 'price_asc':
                products = products.order_by('price')
                sort_friendly = 'Price Ascending'
            elif sortkey == 'price_desc':
                sort_direction = '-price'
                products = products.order_by(sort_direction)
                sort_friendly = 'Price Descending'
            else:
                products = products.order_by('category')
                current_sorting = 'Category'

    context = {
        'products': products,
        'search_term': query,
        'category_friendly': category_friendly,
        'current_category': current_category,
        'sort_friendly': current_sorting,
        'current_sorting': sortkey,

    }

    return render(request, 'products/products.html', context)


def add_product(request):
    """ View for adding products to the store """
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added to store.')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Unable to add product. Ensure there are no errors in the form.')
    else:
        form = AddProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)