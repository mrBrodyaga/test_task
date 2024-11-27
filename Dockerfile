FROM python:3.13.0

WORKDIR /app

COPY requirements.txt .
COPY entrypoint.sh .
RUN pip install -r requirements.txt

COPY . /app/
# Делаем файл entrypoint.sh исполняемым
RUN chmod +x entrypoint.sh

CMD ["/app/entrypoint.sh", "python", "handbook_materials/manage.py", "runserver", "0.0.0.0:8000"]
