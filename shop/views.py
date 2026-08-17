from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models import Count


def product_list(request):

    products = Product.objects.filter(
        available=True
    )

    search = request.GET.get('search')
    category_id = request.GET.get('category')

    if search:
        products = products.filter(
            name__icontains=search
        )

    if category_id:
        products = products.filter(
            category_id=category_id
        )

    categories = Category.objects.annotate(
        product_count=Count('products')
    )

    return render(
        request,
        'shop/product/list.html',
        {
            'products': products,
            'categories': categories,
            'search': search,
        }
    )


def product_detail(request, id, slug):

    product = get_object_or_404(
        Product,
        id=id,
        slug=slug,
        available=True
    )

    return render(
        request,
        'shop/product/detail.html',
        {
            'product': product
        }
    )


def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('/')

    else:

        form = UserCreationForm()

    return render(
        request,
        'registration/register.html',
        {
            'form': form
        }
    )