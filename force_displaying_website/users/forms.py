from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


class EmailAuthForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(EmailAuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Email address'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
