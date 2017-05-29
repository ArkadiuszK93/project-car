from django import forms

from .models import Samochod

class CarForm(forms.ModelForm):

    class Meta:
        model = Samochod
        fields = ('marka', 'model',)