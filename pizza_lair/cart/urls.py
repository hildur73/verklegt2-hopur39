from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="cart-index"),
    path("add_to_cart/<int:item_id>", views.add_to_cart, name='add_to_cart'),
    path('checkout', views.checkout, name='checkout'),
    path('payment', views.payment, name='payment'),
    path('delete_cart', views.delete_cart, name='delete_cart'),
    path('review_site', views.review_site, name='review_site'),
    path('checkout_site', views.checkout_site, name='checkout_site'),
]