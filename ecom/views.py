from django.shortcuts import redirect, render,get_object_or_404
from .models import Product, Category, Customer, Order, OrderItem, Cart, CartItem, Review
from .forms import ProductForm,UserRegistrationForm,CustomerForm,ReviewForm

#CategoryForm, CustomerForm, OrderForm, OrderItemForm, CartForm, CartItemForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout

# Create your views here.
def index(request):
    return render(request, 'index.html')

# ------------- PRODUCT -------------
def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'product_list.html', {'products': products}) 


@login_required
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

@login_required
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
    
@login_required
    #To delete the product
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'delete_product.html', {'product': product})

#User Registration
def register(request):
    if request.method=='POST':
        form =UserRegistrationForm(request.POST)
    
        if form.is_valid():
            user=form.save(commit=False)    
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
    

    else:
        form =UserRegistrationForm()
        

    return render(request, 'registration/register.html', {'form': form})


#To search the product
def search_product(request):
    query = request.GET.get('search')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    
    return render(request, 'search.html', {'query': query, 'products': products})



####################################################################
# ------------- CUSTOMER -------------
@login_required
def customer_detail(request):
    customer = get_object_or_404(Customer, user=request.user)
    return render(request, 'customer_detail.html', {'customer': customer})

@login_required
def customer_edit(request):
    customer = get_object_or_404(Customer, user=request.user)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_detail')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer_edit.html', {'form': form})


# ------------- CATEGORY -------------
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    products = Product.objects.filter(category=category)
    return render(request, 'category_detail.html', {'category': category, 'products': products})






# ------------- CART -------------
@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart_detail.html', {'cart': cart})



@login_required
def cart_add_item(request, product_id):
    cart, created = Cart.objects.get_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_detail')

@login_required
def cart_remove_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('cart_detail')


# ------------- ORDER -------------
@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order_list.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'order_detail.html', {'order': order})

@login_required
def order_create(request):
    cart = get_object_or_404(Cart, user=request.user)
    if request.method == 'POST':
        order = Order.objects.create(
            user=request.user,
            shipping_address=request.POST['shipping_address'],
            total_price=sum(item.quantity * item.product.price for item in cart.items.all())
        )
        for item in cart.items.all():
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity, price=item.product.price)
        cart.items.all().delete()
        return redirect('order_list')
    return render(request, 'order_create.html')


# ------------- REVIEW -------------
@login_required
def review_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ReviewForm()
    return render(request, 'review_add.html', {'form': form, 'product': product})

