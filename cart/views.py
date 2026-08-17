from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from .cart import Cart

def cart_add(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(
        Product,
        id=product_id,
        available=True
    )

    quantity = int(request.POST.get('quantity', 1))

    if product.stock <= 0:
        return redirect('cart:cart_detail')

    if quantity > product.stock:
        quantity = product.stock

    cart.add(
        product,
        quantity
    )

    return redirect('cart:cart_detail')


def cart_update(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(
        Product,
        id=product_id,
        available=True
    )

    quantity = int(request.POST.get('quantity', 1))

    if quantity <= 0:
        cart.remove(product)

    else:
        if quantity > product.stock:
            quantity = product.stock

        cart.add(
            product,
            quantity,
            override_quantity=True
        )

    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    cart.remove(product)

    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)

    return render(request, 'cart/detail.html', {
        'cart': cart
    })