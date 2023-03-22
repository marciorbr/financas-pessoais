from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import LoginForm

def login_view(request):

    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Credênciais inválidas'
        else:
            msg = 'Erro na validação do formulário'

    return render(request, "registration/login.html", {"form": form, "msg": msg})