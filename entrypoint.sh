#!/bin/bash


# Выполнение миграций
python handbook_materials/manage.py makemigrations
python handbook_materials/manage.py migrate

# Загрузка фикстур
python handbook_materials/manage.py loaddata db.json
 
# Запуск основного процесса приложения
exec "$@"