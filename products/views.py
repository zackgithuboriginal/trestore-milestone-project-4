from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Product, Category
from .forms import AddProductForm


def all_products(request):
    """
    View displays products page with all products except for
    sponsorship packages

    Accepts request object as argument to allow for
    sorting and filtering of products from the store page
    """

    products = Product.objects.exclude(category__name='sponsorship')
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
            if not query and not request.GET['product-filter'] and not request.GET['product-sort']:
                messages.error(request,
                               "You didn't enter any search criteria!")

            queries = Q(product_name__icontains=query) | Q(
                        product_description__icontains=query)
            products = products.filter(queries)

        if 'product-sort' in request.GET:
            sortkey = request.GET['product-sort']
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
        else:
            products = products.order_by('price')
            current_sorting = 'Price Ascending'
    else:
        products = products.order_by('price')

    context = {
        'products': products,
        'search_term': query,
        'category_friendly': category_friendly,
        'current_category': current_category,
        'sort_friendly': current_sorting,
        'current_sorting': sortkey,

    }

    return render(request, 'products/products.html', context)


def sponsorship_packages(request):
    """
    View renders the products page with only
    products with a category of sponsorship
    """

    sponsorship_packages = Product.objects.filter(category__name='sponsorship')

    context = {
        'sponsorship_packages': sponsorship_packages,
    }

    return render(request, 'products/sponsorship_packages.html', context)


def product_details(request, product_id):
    """
    The view to render the product details page for a product

    Accepts product_id and request object
    as arguments to pass the required product
    as context to the product details page
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)


@login_required
def add_product(request):
    """
    View to either render the add product page,
    or handle the add product post request

    Accepts request object as argument which provides access to the
    add product form data.

    Requires user to be logged in to access,
    if user is not a superuser they will receive an error message
    and be redirected

    When the view recieves a post request, it takes the form data
    and passes it to the AddProductForm to check if it meets requirements

    The form then gets saved as a new product and the user is redirected
    to the product details page for that product
    """
    if not request.user.is_superuser:
        messages.error(request, 'Oops, you need to be authorised to do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added to store.')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request,
                           'Unable to add product. '
                           'Ensure there are no errors in the form.')
    else:
        form = AddProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    View to either render the edit product page,
    or handle the edit product post request

    Accepts request object and product id as argument which provides access to
    the add product form data and allows view to access the
    correct product object.

    Requires user to be logged in to access,
    if user is not a superuser they will receive an error message
    and be redirected

    When the view recieves a post request, it takes the form data
    and passes it to the AddProductForm along with the relevant product object,
    to check if it meets requirements

    The form then gets saved to update the object and the user is redirected
    to the product details page for that product
    """
    if not request.user.is_superuser:
        messages.error(request, 'Oops, you need to be authorised to do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request,
                             f'{product.product_name} product '
                             'successfully updated.')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request,
                           'Unable to update product.'
                           ' Ensure there are no errors in the form.')
    else:
        form = AddProductForm(instance=product)
        messages.info(request, f'Now editing {product.product_name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    View that handles the deletion of a product object

    Accepts request object and product id as arguments which allows
    the view to access the correct product object.

    Requires user to be logged in to access,
    if user is not a superuser they will receive an error message
    and be redirected

    View gets the correct object and deletes it, then redirects user
    """
    if not request.user.is_superuser:
        messages.error(request, 'Oops, you need to be authorised to do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    store_location = product.category.name
    product.delete()

    messages.success(request, 'Product successfully deleted from the store.')

    if store_location != 'sponsorship':
        return redirect(reverse('products'))
    else:
        return redirect(reverse('sponsorship_packages'))
