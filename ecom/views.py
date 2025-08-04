from django.shortcuts import redirect, render,get_object_or_404
from .models import Product, Category, Customer, Order, OrderItem, Cart, CartItem, Review
from .forms import ProductForm 
#CategoryForm, CustomerForm, OrderForm, OrderItemForm, CartForm, CartItemForm, ReviewForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

# Prod
def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'product_list.html', {'products': products}) 

# To add product into the website from the seller side
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product=form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('product_list')
        
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


#To edit the product
def edit_product(request,id):
    product=get_object_or_404(Product,pk=id,user=request.user )
    if request.method=='POST':
        form = ProductForm(request.POST, request.FILES,instance=product)
        
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('product_list')

    else:
        form=ProductForm(instance=product)
        return render(request, 'add_product.html', {'form': form})
    

    #To delete the product
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'delete_product.html', {'product': product})