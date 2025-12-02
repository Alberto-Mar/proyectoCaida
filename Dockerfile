FROM python:3.10

WORKDIR /code

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN adduser --disabled-password --gecos '' django_user

COPY . /code/

USER django_user
    
CMD ["gunicorn", "--chdir", "/code/pro_caida", "bd-caida.wsgi:application", "--bind", "0.0.0.0:8000"]