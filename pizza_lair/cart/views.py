from django.http import JsonResponse
from django.shortcuts import render
from cart.models import Cart,CartItem
from menu.models import Menu


# Create your views here.
def index(request):
    return render(request, 'cart/index.html')


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
    menu_item.save()
    return render(request, 'cart/index.html')
