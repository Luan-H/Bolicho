from django.contrib import admin
from .models import Produto

class ProdutoAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug' : ('nome',)
    }
    list_display = ['nome', 'slug', 'descricao', 'preco', 'estoque', 'esta_disponivel']
admin.site.register(Produto, ProdutoAdmin)