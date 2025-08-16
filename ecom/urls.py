from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.product_list,name='product_list'),
    path("add_product/", views.add_product, name='add_product'),
    path("edit_product/<int:id>/", views.edit_product, name='edit_product'),
    path("delete_product/<int:id>/", views.delete_product, name='delete_product'),
    path("register/", views.register, name='register'),
    path("ecom/search/", views.search_product, name='search_product'),
    path('categories/', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    # ------------- CART -------------
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.cart_add_item, name='cart_add_item'),
    path('cart/remove/<int:item_id>/', views.cart_remove_item, name='cart_remove_item'),
    # ------------- ORDER -------------
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('order/create/', views.order_create, name='order_create'),
    # ------------- REVIEW -------------
    path('review/add/<int:product_id>/', views.review_add, name='review_add'),
    # ------------- CUSTOMER -------------
    path('customer/', views.customer_detail, name='customer_detail'),
    path('customer/edit/', views.customer_edit, name='customer_edit'),

    path("index/", views.index, name='index'),

]