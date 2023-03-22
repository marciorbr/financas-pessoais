from django import forms
from .models import Usuario


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "email@email.com",
                "class": "form-control form-control-sm"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control form-control-sm"
            }
        ))


    class Meta:
        model = Usuario
        fields = ('email', 'primeiro_nome', 'password1', 'password2')