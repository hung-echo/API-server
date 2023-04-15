# API-server
first API

You can read and practice to write API in link which used to learn to write this API
# https://www.bezkoder.com/django-rest-api/
Learn more about data type and fields list in below link
# https://www.geeksforgeeks.org/django-model-data-types-and-fields-list/

--I wrote API with Django so you must install:

1. pip install django

2. pip install djangorestframework

3. pip install django-cors-headers

4. pip install pyodbc

5. pip install django-pyodbc-azure

-- Open code by: code .
-- You can run server with statement : py manage.py runserver

--- Modify file settings:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', # add frame_work installed
    'corsheaders', # add frame_work installed
    'PTticket.apps.PtticketConfig' # add your app with struct name_app.apps.name_class in file apps.py
]

add row: CORS_ORIGIN_ALLOW_ALL = True

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # add this row in here 
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# configure to connect database, I used sql server
DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc', # lib to connect sql server
        'NAME': '', # name of your database
        'USER': '', # name user of sqlserver
        'PASSWORD' : '', # password of sqlserver
        'HOST' : '', # you can take it in sqlserver at properties
        'OPTIONS':{
            'driver' : 'ODBC Driver 17 for SQL Server'
        }
    }
}

-- If you meet error which I couldn't save in time while working but I can recommend one of them follows
1. downgrade your django to 2.1.1 like me => pip install django==2.1.1
