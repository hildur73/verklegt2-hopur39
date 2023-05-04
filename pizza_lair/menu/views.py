from django.shortcuts import render
from menu.models import Menu
# Create your views here.

def index(request):
    context = {'menu:': Menu.objects.all().order_by('name')}
    return render(request, 'menu/index.html', context)
