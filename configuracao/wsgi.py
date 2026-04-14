import os
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configuracao.settings')

application = get_wsgi_application()

# Força o Django a criar as tabelas e o admin toda vez que o site iniciar
try:
    print("Iniciando comandos de banco de dados...")
    call_command('migrate', interactive=False)
    
    # Opcional: Se você quiser garantir que o admin seja criado aqui também
    # basta chamar o script que criamos antes:
    import criar_admin 
    
    print("Banco de dados pronto para uso!")
except Exception as e:
    print(f"Erro durante a inicialização: {e}")