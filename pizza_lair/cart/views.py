from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from cart.forms.cart_forms import CheckOutForm, PaymentStepsForm
from cart.models import Cart, CartItem, Country, Checkout, Paymentstep
from menu.models import Menu
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    cart = Cart.objects.filter(user_id=request.user).first()
    items = CartItem.objects.filter(cartid=cart.id)
    all_pizzas = []
    total = 0
    for item in items:
        menuitem = Menu.objects.filter(cartitem=item.id).first()
        all_pizzas.append(menuitem)
        total = menuitem.price + total
    context = {"all_pizzas": all_pizzas, 'total': total}
    return render(request, 'cart/index.html', context)

@login_required
def add_to_cart(request,item_id):
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
    return redirect('cart-index')

@login_required
def checkout(request):
    if request.method == 'POST':
        form = CheckOutForm(data=request.POST)

        if form.is_valid():
            checkout = form.save(commit=False)
            checkout.user_id = request.user
            checkout.save()
            return redirect('payment')
    else:
        form = CheckOutForm()
    return render(request,'cart/checkout.html',{
        'form': form
    })


@login_required
def payment(request):
    if request.method == 'POST':
        form = PaymentStepsForm(data=request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user_id = request.user
            payment.save()
            return redirect('review_site')
    else:
        form = PaymentStepsForm()
    return render(request,'cart/payment.html',{
        'form': form
    })

@login_required
def delete_cart(request):
    cart = Cart.objects.get(user_id=request.user, payment=False)
    for cart_item in cart.cartitem_set.all():
        cart_item.delete()
    return redirect('cart-index')

@login_required()
def review_site(request):
    cart = Cart.objects.filter(user_id=request.user).first()
    items = CartItem.objects.filter(cartid=cart.id)
    checkout = Checkout.objects.filter(user_id=request.user).first()
    payment = Paymentstep.objects.filter(user_id=request.user).first()
    context = {
        'fullname': checkout.fullname,
        'streetname': checkout.streetname,
        'city': checkout.city,
        'postalcode': checkout.postalcode,
        'cardholder': payment.cardholder,
        'cardnumber': payment.cardnumber,
        'experitiondate': payment.expirationdate,
    }
    return render(request, 'cart/review_step.html', context)

@login_required()
def checkout_site(request):
    delete_cart(request)
    return render(request, 'cart/checkout_site.html')
