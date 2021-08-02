
from .models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields, models

from django.contrib.auth.models import User

# ******************** SignUpForm ****************
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1' , 'password2']


# ******************** U_info_form****************
class U_info_form(forms.ModelForm):
    class Meta:
        model=User
        fields = ['username','first_name' , 'last_name' , 'email']
        # widgets={
        # 'username':forms.TextInput(attrs={'class':'form-control'}),
        # 'first_name':forms.TextInput(attrs={'class':'form-control'}),
        # 'last_name':forms.TextInput(attrs={'class':'form-control'}),
        # 'email':forms.EmailInput(attrs={'class':'form-control'})

        # }

# ******************** P_info_form****************
class P_info_form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city' , 'phone','bio','image',]
        # widgets={
	       #  'street':forms.TextInput(attrs={'class':'form-control'}),
	       #  'city':forms.Select(attrs={'class':'form-control'}),
	       #  'bio':forms.TextInput(attrs={'class':'form-control'}),
	       

        # }


