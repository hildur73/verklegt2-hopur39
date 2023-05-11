from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="cart-index"),
    path("add_to_cart/<int:item_id>", views.add_to_cart, name='add_to_cart'),
    path('checkout', views.checkout, name='checkout'),
    path('payment', views.payment, name='payment'),
]