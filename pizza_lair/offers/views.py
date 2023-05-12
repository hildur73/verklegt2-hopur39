from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from offers.forms.offers_form import OffersCreateForm, OffersUpdateForm
from offers.models import Offers
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def index(request):
    """This function gets all the offers from the database and displays them on the offers page"""
    context = {}
    context['offers'] = Offers.objects.all()
    return render(request, 'offers/index.html', context)

@login_required
def create_offers(request):
    """This function handles the creation of a new offer. When a new offer is made it redirects the user
    to the offer page"""
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

@login_required
def get_offer_by_id(request, id):
    """This function gets the offers by id from the database and displays them on the offer site """
    bla = Offers.objects.filter(id=id).first()
    return render(request, 'offers/offer_details.html', {
        'offers': get_object_or_404(Offers, pk=id)
    })


@login_required
def delete_offers(request, id):
    """This function allows the user to delete a specific offer from the database. Then it redirects the user
    to the offers index page"""
    offers = get_object_or_404(Offers, pk=id)
    offers.delete()
    return redirect('offers-index')

@login_required
def update_offers(request, id):
    """This function allows the user to update an offer and then redirects the user to offers page """
    instance = get_object_or_404(Offers, pk=id)
    if request.method == 'POST':
        form = OffersUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            offers = form.save()
            return redirect('offers-index')
    else:
        form = OffersUpdateForm(instance=instance)
    return render(request, 'offers/update_offers.html', {
        'form': form,
        'id': id
    })


