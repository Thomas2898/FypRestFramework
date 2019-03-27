FROM python:3.7
MAINTAINER Thomas
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install libgdal-dev
RUN mkdir -p /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install --upgrade pip
RUN pip install Django==2.1.2
RUN pip install django-cors-headers==2.4.0
RUN pip install django-leaflet==0.24.0
RUN pip install djangorestframework==3.9.0
RUN pip install djangorestframework-gis==0.13
RUN pip install psycopg2==2.7.5
RUN pip install requests==2.20.0
RUN pip install pygments

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]