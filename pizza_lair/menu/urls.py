from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="menu-index"),
    path('<int:id>', views.get_pizza_by_id, name='menu_details')
]