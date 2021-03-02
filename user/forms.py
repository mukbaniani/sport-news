from django.contrib.auth.forms import UserCreationForm
from user.models import Account
from django import forms


class UserRegister(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = Account
        fields = ['username', 'email', 'password1', 'password2']