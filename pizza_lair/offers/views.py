from django.shortcuts import render, redirect

from offers.forms.offers_form import OffersCreateForm
from offers.models import Offers

# Create your views here.
def index(request):
    context = {}
    context['offers'] = Offers.objects.all()
    return render(request, 'offers/index.html', context)


def create_offers(request):
    if request.method == 'POST':
        form = OffersCreateForm(data=request.POST)
        if form.is_valid():
            menu = form.save()
            return redirect('offers-index')
    else:
        form = OffersCreateForm()
    return render(request, 'offers/create_offers.html', {
        'form':form
    })