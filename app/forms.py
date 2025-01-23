from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Donor

class UserForm(UserCreationForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class':'form-control',
    'placeholder':'enter password'}))
    password2 =  forms.CharField(label='confirm password(again)', widget=forms.PasswordInput(attrs={'class':'form-control',
    'placeholder':'enter password again'}))
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter Last Name'}),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
            'email':forms.EmailInputInput(attrs={'class':'form-control','placeholder':'Email ID'}),
        }
    
class DonorSignupForm(forms.ModelForm):
    userpic = forms.ImageField(widget=forms.TextInput(attrs={'class': 'form-control'})),
    class Meta:
        model=Donor
        fields=['contact','userpic', 'address']
        widgets={
            'contact': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Contact Number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Full Address'})
        }