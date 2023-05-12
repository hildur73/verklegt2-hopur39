from django.http import JsonResponse
from django.shortcuts import render, redirect

from cart.forms.cart_forms import CheckOutForm, PaymentStepsForm
from cart.models import Cart, CartItem, Country
from menu.models import Menu
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    """This function shows the items in the user's cart."""
    cart = Cart.objects.filter(user_id=request.user).first()
    items = CartItem.objects.filter(cartid=cart.id)
    all_pizzas = []
    for item in items:
        menuitem = Menu.objects.filter(cartitem=item.id).first()
        all_pizzas.append(menuitem)
    context = {"all_pizzas": all_pizzas}
    return render(request, 'cart/index.html',context)

@login_required
def add_to_cart(request,item_id):
    """This function adds the items that the user has selected to the cart"""
    the_cart = None
    my_cart = Cart.objects.filter(user_id=request.user, payment=False)
    if len(my_cart) == 0:
        new_cart = Cart()
        new_cart.user_id = request.user
        new_cart.payment = False
        new_cart.save()
        the_cart = new_cart
    else:
        the_cart = my_cart[0]
    new_item = CartItem()
    new_item.cartid = the_cart
    menu_item = Menu.objects.filter(id=item_id).first()
    new_item.menuid = menu_item
    new_item.save()
    menu_item.save()
    return render(request, 'cart/index.html')

@login_required
def checkout(request):
    """This function displays the checkout form and saves the data"""
    if request.method == 'POST':
        form = CheckOutForm(data=request.POST)
        if form.is_valid():
            checkout = form.save()
            return redirect('payment')
    else:
        form = CheckOutForm()
    return render(request,'cart/checkout.html',{
        'form': form
    })


@login_required
def payment(request):
    """Ths function displayes a payment form and saves the data"""
    if request.method == 'POST':
        form = PaymentStepsForm(data=request.POST)
        if form.is_valid():
            payment = form.save()
            return redirect('cart-index')
    else:
        form = PaymentStepsForm()
    return render(request,'cart/payment.html',{
        'form': form
    })
