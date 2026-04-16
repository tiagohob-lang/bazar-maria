from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import vitrine, detalhe_produto
from django.contrib.auth.models import User

# Tenta criar o admin se ele não existir
try:
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'tiagohob@gmail.com', 'Galo@2013')
except:
    pass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vitrine, name='vitrine'), # Página inicial da loja
    path('produto/<int:pk>/', detalhe_produto, name='detalhe_produto'), # Detalhes do produto
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Adicione isso logo abaixo da lista urlpatterns:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)