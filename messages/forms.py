from django.contrib.auth.models import User
from .models import Contact, Message
from django import forms
from django.db import models

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

class AddContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['owner', 'contact']

class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message_text']
