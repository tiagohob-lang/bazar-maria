from django.contrib import admin
from .models import Publico, TipoRoupa, Tamanho, Cor, Produto, ImagemProduto

admin.site.register(Publico)
admin.site.register(TipoRoupa)
admin.site.register(Tamanho)
admin.site.register(Cor)

class ImagemProdutoInline(admin.TabularInline):
    model = ImagemProduto
    extra = 4  # Quantidade de campos vazios para fotos novas que aparecerão

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    inlines = [ImagemProdutoInline]

# Dica extra: Isso ajuda a ver os detalhes na lista do Admin sem abrir o produto
    list_display = ('titulo', 'publico', 'tipo', 'preco', 'em_destaque')
    list_filter = ('publico', 'tipo', 'em_destaque')
    search_fields = ('titulo', 'descricao')