"""
Django admin customization.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models
from core.models import Categoria, Produto, ProdutoVariacao, User


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'ativo',
    )
    list_filter = (
        'ativo',
        'categorias',
    )
    search_fields = (
        'nome',
        'descricao',
    )
    ordering = ('nome',)
    list_per_page = 10


@admin.register(ProdutoVariacao)
class ProdutoVariacaoAdmin(admin.ModelAdmin):
    list_display = (
        'produto',
        'tamanho',
        'preco',
    )
    list_filter = (
        'tamanho',
        'preco',
    )
    search_fields = ('produto__nome',)
    ordering = (
        'produto',
        'preco',
    )
    list_per_page = 10


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    ordering = ('nome',)
    list_per_page = 10


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    ordering = ['id']
    list_display = ['email', 'name', 'telefone', 'nascimento']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Personal Info'),
            {
                'fields': (
                    'name',
                    'telefone',
                    'nascimento',
                    'foto',
                )
            },
        ),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            },
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
        (_('Groups'), {'fields': ('groups',)}),
        (_('User Permissions'), {'fields': ('user_permissions',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'name',
                    'telefone',
                    'nascimento',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                ),
            },
        ),
    )


admin.site.register(models.Endereco)
admin.site.register(models.Avaliacao)
admin.site.register(models.Pedido)
admin.site.register(models.Pagamento)
admin.site.register(models.Embalagem)
admin.site.register(models.ItemPedido)
admin.site.register(models.Fita)
admin.site.register(models.Tampa)
admin.site.register(models.TipoProduto)
admin.site.register(models.Recipiente)
admin.site.register(models.Aroma)
admin.site.register(models.Adesivo)
admin.site.register(models.Parafina)
admin.site.register(models.Pavio)
