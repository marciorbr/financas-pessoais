# accounts/models.py
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from .managers import UserManager


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('endereço de email', unique=True)
    primeiro_nome = models.CharField('primeiro nome', max_length=150, blank=True)
    ultimo_nome = models.CharField('último nome', max_length=150, blank=True)
    data_criacao = models.DateTimeField('data de criação', auto_now_add=True)
    is_active = models.BooleanField('ativo', default=True)
    is_admin = models.BooleanField(
        'admin status',
        default=False,
        help_text=
            'Especifica se o usuário pode logar no site admin',
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "O usuário tem uma permissão especifica?"
        return True

    def has_module_perms(self, app_label):
        "O usuário tem pemissão para view app `app_label`?"
        return True

    def get_full_name(self):
        '''
        Retorna o primeiro nome mais o último com espaço entre eles.
        '''
        nome_completo = f'{self.primeiro_nome} {self.ultimo_nome}'
        return nome_completo.strip()

    def get_short_name(self):
        '''
        Retorna primeiro nome do usuário.
        '''
        return self.primeiro_nome

    @property
    def is_staff(self):
        "O usuário é membro de staff?"
        return self.is_admin