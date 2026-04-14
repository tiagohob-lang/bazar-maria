from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import vitrine, detalhe_produto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vitrine, name='vitrine'), # Página inicial da loja
    path('produto/<int:pk>/', detalhe_produto, name='detalhe_produto'), # Detalhes do produto
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)