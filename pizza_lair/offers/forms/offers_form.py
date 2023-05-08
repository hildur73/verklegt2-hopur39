from django.forms import ModelForm, widgets
from offers.models import Offers

class OffersCreateForm(ModelForm):
    class Meta():
        model = Offers
        exclude = ['id']
        widgets = {
            'description': widgets.TextInput(attrs={'class':'form-control'}),
            'price': widgets.NumberInput(attrs={'class':'form-control'})
        }