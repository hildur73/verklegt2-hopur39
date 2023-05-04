from django.shortcuts import render
from offers.models import Offers

# Create your views here.
def index(request):
    context = {'offers:': Offers.objects.all()}
    return render(request, 'offers/index.html', context)