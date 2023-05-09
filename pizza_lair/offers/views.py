from django.shortcuts import render, redirect

from offers.forms.offers_form import OffersCreateForm, OffersUpdateForm
from offers.models import Offers
from django.shortcuts import render, get_object_or_404, redirect

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

def get_offer_by_id(request, id):
    bla = Offers.objects.filter(id=id).first()
    #menudetail = Menudetails.objects.filter(menuid_id=bla.id).first()
    return render(request, 'offers/offer_details.html', {
        'offers': get_object_or_404(Offers, pk=id)
        #'menudetails': menudetail
    })


#@login_required
def delete_offers(request, id):
    offers = get_object_or_404(Offers, pk=id)
    offers.delete()
    return redirect('offers-index')

#@login_required
def update_offers(request, id):
    instance = get_object_or_404(Offers, pk=id)
    if request.method == 'POST':
        form = OffersUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('offers', id=id)
    else:
        form = OffersUpdateForm(instance=instance)
    return render(request, 'offers/update_offers.html', {
        'form': form,
        'id': id
    })
