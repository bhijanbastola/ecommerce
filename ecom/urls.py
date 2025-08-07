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
    path("index/", views.index, name='index'),

]