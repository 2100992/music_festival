from allauth.account.forms import LoginForm
from django import forms
# from .models import *


class UserLoginForm(LoginForm):
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Пароль'
            }
        )
    )
    # class Meta:
    #     model = ""
