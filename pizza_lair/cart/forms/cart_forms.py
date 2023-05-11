from django.forms import ModelForm, widgets
from cart.models import Cart, Checkout, Paymentstep
from django import forms


class CartUpdateForm(ModelForm):
    class Meta:
        model = Cart
        exclude = ['id']
        widgets = {
            ''
        }

class CheckOutForm(ModelForm):
    class Meta:
        model = Checkout
        exclude = ['id']
        widgets = {
            'fullname': widgets.TextInput(attrs={'class':'form-control'}),
            'streetname': widgets.TextInput(attrs={'class':'form-control'}),
            'country': widgets.Select(attrs={'class':'form-control'}),
            'city': widgets.TextInput(attrs={'class':'form-control'}),
            'postalcode': widgets.NumberInput(attrs={'class':'form-control'}),
        }


class PaymentStepsForm(ModelForm):
    class Meta:
        model = Paymentstep
        exclude = ['id']
        widgets = {
            'cardholder': widgets.TextInput(attrs={'class': 'form-control'}),
            'cardnumber': widgets.NumberInput(attrs={'class': 'form-control'}),
            'expirationdate': widgets.TextInput(attrs={'class': 'form-control'}),
            'cvc': widgets.DateInput(attrs={'class': 'form-control'}),
        }