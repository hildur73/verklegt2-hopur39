from django.shortcuts import render, get_object_or_404
from menu.models import Menu, Menudetails
# Create your views here.

def index(request):
    context = {}
    context['menu'] = Menu.objects.all()
    return render(request, 'menu/index.html', context)

def get_pizza_by_id(request, id):
    bla = Menu.objects.filter(id=id).first()

    menudetail = Menudetails.objects.filter(menuid_id=bla.id).first()

    return render(request, 'menu/menu_details.html', {
        'menu': get_object_or_404(Menu, pk=id),
        'menudetails': menudetail
    })
