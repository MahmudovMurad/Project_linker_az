from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

  
from django import forms

from django.contrib.auth import get_user_model, password_validation
from django.db.models.fields.related import OneToOneField
from django.forms.fields import CharField
from django.shortcuts import render
from .models import *
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import (
    PasswordChangeForm, UserCreationForm, UsernameField, AuthenticationForm,PasswordResetForm,SetPasswordForm
)
class LoginForm(forms.Form):
    username= forms.CharField(max_length=50, label='Mail', required=True, widget=forms.TextInput(attrs={'type': 'email'}))
    password= forms.CharField(max_length=50, label='Parol', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Istifadeci adi ve ya sifre yanlisdi')

        return super(LoginForm, self).clean()

    def __init__(self, *args, **kwargs):
        super(LoginForm,self).__init__(*args, **kwargs)

        
        self.fields['username'].widget.attrs= {'class': 'w-75  pl-2 border-0', 'placeholder': 'E-mail'}
        self.fields['password'].widget.attrs = {'placeholder': 'Parol', 'class': 'w-75  pl-2 border-0'}
        



class RegisterForm(forms.ModelForm):
    
    username= forms.CharField(max_length=50, label='Mail:', widget=forms.TextInput(attrs={'type': 'email'}))
    password1= forms.CharField(max_length=20, label='Parol:', widget=forms.TextInput(attrs={'type': 'password'}))
    password2= forms.CharField(max_length=20, label='Parol təkrar:', widget=forms.TextInput(attrs={'type': 'password'}))
    

    class Meta:
        model= User

        fields=[            
            'username',
            'password1',
            'password2',

        ]

    def __init__(self, *args, **kwargs):
        super(RegisterForm,self).__init__(*args, **kwargs)

        
        self.fields['username'].widget.attrs= {'class': 'w-75  pl-2 border-0', 'placeholder': 'E-mail'}
        self.fields['password1'].widget.attrs = {'placeholder': 'Parol', 'class': 'w-75  pl-2 border-0', 'type': 'password'}
        self.fields['password2'].widget.attrs = {'placeholder': 'Parol (təkrar)', 'class': 'w-75  pl-2 border-0', 'type': 'password'}




