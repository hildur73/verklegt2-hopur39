from django.forms import ModelForm, widgets
from menu.models import Menu
from django import forms


class MenuUpdateForm(ModelForm):
    description = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Menu
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'image': widgets.TextInput(attrs={'class': 'form-control'})
        }


class MenuCreateForm(ModelForm):
    description = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:

        model = Menu
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class':'form-control'}),
            'price': widgets.NumberInput(attrs={'class':'form-control'}),
            'image': widgets.TextInput(attrs={'class':'form-control'}),
        }

