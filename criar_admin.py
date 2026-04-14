import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configuracao.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
username = 'admin' # Escolha seu usuario
email = 'tiagohob@gmail.com'
password = 'Galo@2013' # Mude esta senha!

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("Superusuário criado com sucesso!")
else:
    print("Superusuário já existe.")