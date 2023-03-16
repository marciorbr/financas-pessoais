# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Usuario


class UserAdmin(BaseUserAdmin):

    list_display = ('email', 'primeiro_nome', 'ultimo_nome', 'is_admin', 'is_active', 'data_criacao')  # noqa E501
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações pessoais', {'fields': ('primeiro_nome', 'ultimo_nome')}),
        ('Permissões', {
            'fields': (
                'is_active',
                'is_admin',
                'groups',
                'user_permissions',
            )
        }),
        ('Dados importantes', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'primeiro_nome', 'ultimo_nome')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(Usuario, UserAdmin)
