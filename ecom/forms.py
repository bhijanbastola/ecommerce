from django import forms
from .models import Product, Category, Customer, Order, OrderItem, Cart, CartItem, Review
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'category', 'image']