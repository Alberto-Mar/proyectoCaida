FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY ./pro_caida /code
ADD requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN chmod -R +x /code/scripts_docker/
RUN adduser --disabled-password --gecos '' django_user
RUN chown -R django_user:django_user /code && chmod -R 755 /code
USER django_user