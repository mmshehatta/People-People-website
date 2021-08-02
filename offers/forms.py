from django import forms

from .models import *




class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = '__all__'
        exclude = ('slug','date','owner')



