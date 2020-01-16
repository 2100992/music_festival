from allauth.account.forms import LoginForm, SignupForm
from django import forms
from django.forms import formset_factory
# from .models import *

# class TstLoginForm(forms.ModelForm):
#     class Meta:
#         model = 

class UserLoginForm(LoginForm):
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Пароль'
            }
        )
    )



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

#     ChangePasswordForm

# AddEmailForm


# UserForm

LoginSignupFormset = formset_factory(UserLoginForm, UserSignupForm)