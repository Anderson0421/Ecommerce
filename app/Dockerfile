#Imagen original

FROM python:3.9.6-alpine

#Servidor - Directorio de trabajo / Working directory

WORKDIR /usr/src/app

#Configurar las variables de entorno!

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --update --no-cache mariadb-connector-c-dev \
    && apk add --no-cache --virtual .build-deps \
    mariadb-dev \
    gcc \
    musl-dev \
    && pip install mysqlclient==1.4.2.post1 \
    && apk del .build-deps \
    && apk add libffi-dev openssl-dev libgcc


#Depedencias del proyecto / Instalar depedencias

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#Copiamos todo el proyecto a la imagen

COPY . .

# CMD python manage.py runserver

# EXPOSE 8000







