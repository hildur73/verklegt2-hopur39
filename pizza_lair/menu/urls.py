from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="menu-index"),
    path('<int:id>', views.get_pizza_by_id, name='menu_details'),
    path('create_menu', views.create_menu, name='create_menu'),
    path('delete_menu/<int:id>', views.delete_menu, name='delete_menu'),
    path('update_menu/<int:id>', views.update_menu, name='update_menu'),
]
