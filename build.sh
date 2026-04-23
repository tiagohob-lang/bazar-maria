#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

# Detecta mudanças novas
python manage.py makemigrations --no-input

# Tenta aplicar ignorando conflitos de tabelas já existentes
python manage.py migrate --fake-initial --no-input