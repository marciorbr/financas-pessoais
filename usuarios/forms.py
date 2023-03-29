from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "email@mail.com",
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

class CadastroUsuarioForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "email@mail.com",
                "class": "form-control"
            }
        )
    )
    primeiro_nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    ultimo_nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    class Meta:
        model = Usuario
        fields = ('email','primeiro_nome', 'ultimo_nome', 'password1', 'password2')