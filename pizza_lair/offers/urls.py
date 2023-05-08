from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="offers-index"),
    path('create_offers', views.create_offers, name='create_offers')
]