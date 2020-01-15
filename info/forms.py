from allauth.account.forms import LoginForm, SignupForm
from django import forms
from django.forms import formset_factory
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


class UserSignupForm(SignupForm):
    # pass
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Пароль'
            }
        )
    )

LoginSignupFormset = formset_factory(UserLoginForm, UserSignupForm)