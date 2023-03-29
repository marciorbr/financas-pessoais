from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse

from .forms import LoginForm, CadastroUsuarioForm


# TODO Padronizar template_name = 'register.html'
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


# TODO Configurar menssagens de alertas
def cadastro_view(request):
    
    msg = None
    template_name = 'usuarios/cadastro.html'

    if request.method == "POST":
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('usuarios:login'))
        
        msg = 'Erro ao tentar cadastrar novo usuário'

    form = CadastroUsuarioForm()

    context = {
        'form': form,
        'msg': msg, 
    }

    return render(request, template_name, context)