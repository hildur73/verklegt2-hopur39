from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from menu.forms.menu_form import MenuCreateForm, MenuUpdateForm
from menu.models import Menu, Menudetails


# Create your views here.

def index(request):
    #works with a questionmark after /
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        pizzas = [{
            'id':x.id,
            'name':x.name,
            'image':x.image,
        } for x in Menu.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': pizzas})
    context = {}
    context['menu'] = Menu.objects.all().order_by('name')
    return render(request, 'menu/index.html', context)


def get_pizza_by_id(request, id):
    bla = Menu.objects.filter(id=id).first()
    menudetail = Menudetails.objects.filter(menuid_id=bla.id).first()
    return render(request, 'menu/menu_details.html', {
        'menu': get_object_or_404(Menu, pk=id),
        'menudetails': menudetail
    })


def create_menu(request):
    if request.method == 'POST':
        form = MenuCreateForm(data=request.POST)
        if form.is_valid():
            menu = form.save()
            menu_description = Menudetails(description=request.POST['description'], menu=menu)
            menu_description.save()
            return redirect('menu-index')
    else:
        form = MenuCreateForm()
    return render(request, 'menu/create_menu.html', {
        'form': form
    })


def delete_menu(request, id):
    menu = get_object_or_404(Menu, pk=id)
    menu.delete()
    return redirect('menu-index')


def update_menu(request, id):
    instance = get_object_or_404(Menu, pk=id)
    if request.method == 'POST':
        form = MenuUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('menu_details', id=id)
    else:
        form = MenuUpdateForm(instance=instance)
    return render(request, 'menu/update_menu.html', {
        'form': form,
        'id': id,
    })
