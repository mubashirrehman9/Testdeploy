from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, UsernameField, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms import TextInput, EmailInput, PasswordInput, ModelForm
from .models import Contact, Review
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext, gettext_lazy, ugettext_lazy as _

from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm


class RatingForm(ModelForm):
    # rating = forms.Widget(attrs={'type': "hidden"})
    class Meta:
        model = Review
        fields = ['name', 'title', 'review', 'rating']

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'review': forms.Textarea(attrs={'class': 'form-control'}),
            'rating': forms.HiddenInput(attrs={'class': 'form-control'}),

        }


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'subject': TextInput(attrs={'class': 'form-control'}),

        }


class UserReg(UserCreationForm):
    password2 = forms.CharField(label='again', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'username': {
                'required': ("ENTER A NAME"),
            },
        }


class FirstloginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}),
    )


class ChangeForm(PasswordChangeForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
    )

    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control'}),
    )

    field_order = ['old_password', 'new_password1', 'new_password2']


class NewpasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
    )


class EditUserProfileform(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login']
