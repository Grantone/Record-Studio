from django import forms
from .models import *
from django.forms import widgets


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        exclude = ['user', ]
        fields = ('name', 'phone', 'location')
