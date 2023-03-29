# accounts/urls.py
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
]
