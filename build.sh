#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input

# O comando migrate vai usar o novo 0001_initial.py
python manage.py migrate --fake-initial --no-input