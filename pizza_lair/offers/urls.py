from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="offers-index"),
    path('<int:id>', views.get_offer_by_id, name='offer_details'),
    path('create_offers', views.create_offers, name='create_offers'),
    path('delete_offers/<int:id>', views.delete_offers, name='delete_offers'),
    path('update_offers/<int:id>', views.update_offers, name='update_offers'),
]
