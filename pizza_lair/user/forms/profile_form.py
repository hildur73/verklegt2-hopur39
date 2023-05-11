from django.forms import ModelForm, widgets
from user.models import Profile
from django import forms


class ProfileForm(ModelForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Profile
        exclude = ['id','user']
        widgets = {
            'profile_image': widgets.TextInput(attrs={'class':'form-control'})
        }

