from django.shortcuts import render, redirect, get_object_or_404
from menu.models import MenuItem
from .cart import Cart
from .forms import CartAddForm

# Create your views here.

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddForm(initial={
            'quantity': item['quantity'],
            'update': True,
        })
    return render(request, 'cart/cart_detail.html', {'cart': cart})

def cart_add(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(MenuItem, id=item_id)
    form = CartAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(item=item, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart_detail')

def cart_remove(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(MenuItem, id=item_id)
    cart.remove(item)
    return redirect('cart_detail')

def checkout(request):
    if request.method == 'POST':
        # handle payment or proof upload
        return redirect('order_success')
    return render(request, 'cart/cart_checkout.html')

def order_success(request):
    return render(request, 'cart/order_success.html')  
