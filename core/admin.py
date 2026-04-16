from django.contrib import admin
from .models import Publico, TipoRoupa, Tamanho, Produto

admin.site.register(Publico)
admin.site.register(TipoRoupa)
admin.site.register(Tamanho)
admin.site.register(Produto)