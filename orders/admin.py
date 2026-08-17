from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):

    model = OrderItem

    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
    'id',
    'first_name',
    'last_name',
    'email',
    'city',
    'payment_method',
    'status',
    'paid',
    'created',
   ]

    list_filter = [
    'status',
    'paid',
    'payment_method',
    'created',
   ] 
    list_editable = [
    'status',
    'paid',
    ]

    search_fields = [
        'first_name',
        'last_name',
        'email',
    ]

    inlines = [
        OrderItemInline,
    ]