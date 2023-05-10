from django.forms import ModelForm, widgets
from cart.models import Cart
from django import forms


class CartUpdateForm(ModelForm):
    class Meta:
        model = Cart
        exclude = ['id']
        widgets = {
            ''
        }