from django.contrib import admin
from django.urls import path
from .models import Product, Category, Customer, Order, OrderItem,Cart,CartItem,Review

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Review)

