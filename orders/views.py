from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction

from cart.cart import Cart

from .forms import OrderCreateForm
from .models import Order, OrderItem


@login_required
def order_create(request):

    cart = Cart(request)

    if len(cart) == 0:
        return redirect('/')

    if request.method == 'POST':

        form = OrderCreateForm(request.POST)

        if form.is_valid():

            with transaction.atomic():

                order = form.save()

                for item in cart:

                    product = item['product']
                    quantity = item['quantity']

                    if quantity > product.stock:
                        quantity = product.stock

                    if quantity <= 0:
                        continue

                    product.stock -= quantity

                    if product.stock == 0:
                        product.available = False

                    product.save()

                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        price=item['price'],
                        quantity=quantity
                    )

                cart.clear()

            return render(
                request,
                'orders/order/created.html',
                {
                    'order': order
                }
            )

    else:

        form = OrderCreateForm()

    return render(
        request,
        'orders/order/create.html',
        {
            'cart': cart,
            'form': form
        }
    )


@login_required
def my_orders(request):

    orders = Order.objects.filter(
        email=request.user.email
    )

    return render(
        request,
        'orders/my_orders.html',
        {
            'orders': orders
        }
    )


@login_required
def order_detail(request, id):

    order = Order.objects.get(
        id=id,
        email=request.user.email
    )

    return render(
        request,
        'orders/order_detail.html',
        {
            'order': order
        }
    )