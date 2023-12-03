# Django-iloveAnime
#############################################################
#framework - 
A framework is a particular set of rules, idea or belief which u use
n order to deal with problem or to decide what to do.

#django is web development framework

High level python web application framework
open source.
follows - Model view Template 

#Why
its fast and simple
its secure
well established.
MVT Support and OOP
Built in Authentication and Authorization.
Packaging system.

#which companies uses it :
Youtube
Instagram
Big bucket
Spotify
#############################################################

# Prerequisite
- HTML, CSS, Bootstrap
- Python Knowladges
- Javascript, Jquery little

#############################################################
# setup Django Project
[Linux]
pip freeze - to see installed packages.
pip3 install django
pip3 install django-admin
django-admin startproject Project_Name
#folder will be created, go inside it
cd Projecy_Name
django-admin startapp APP_NAME
#Development server start
python3 manage.py runserver
python3 manage.py runserver 8080  ( will run on port 8080 )
#First Application
- make 3 folders
tempalates - html pages
statis - js, static images, 
media - dynamic images, files, products etc.
#############################################################

# MVT (Model View Template):
- Software design pattern
Model - data bases table, data manupulation,
View - User interface to render website.
Template - HTML outputs, dynamic contents etc.
USER --> DjangoWebsite --> URLs --> View --> MODEL & Template

#############################################################
# Migrate and Migration
Superuser for db create :
python3 manage.py makemigration  : to make tables using models.
python3 manage.py migrate : apply changes to db 

#DB Browser download for linux
snap install sqlitebrowser --devmode

#Create Super User for DB
localhost:/admin  
python3 manage.py createsuperuser
(pass details)
#############################################################

# Urls and Views
Urls - creating routes for the redirection on page.
https://www.google.com/blogs  --> show blogs page at google.com 
{Urls}/{slug}

Views - on clicking on urls which view will be called.
{ prepare and returns response data }
Function based views - 
Class based views - 


#############################################################
# Create URLs & Views in django
create a view.py file on app folder (folder under project)
in views.py 

import http from httpresponse

def Contact(request):
    return httpresponse("Contact Page)

in urls.py

from Project_Name import views

add this :  path("contact-us/',views.Contact)
#############################################################

# dynamic routes 

Urls changes and redirection on different pages.
3 types - int, str, slug
<int:cust_id>    # 1,3,46,55, etc
<str:cust_name>  # string, strskdshg etc
<slug:value>     # common-test-link, blog-1-sendnig 

urls.py 

path('blogs/<slug:blog_title>',views.blogs)
path('blogs/<blog>',views.blogs)  #all three Supported

views.py

def blogs(request, blog_title):
    return httpresponse(blog_title)

#############################################################

# render html Templates
- Create a folder named as templates
- put htmls files inside it.
- 

settings.py
{ set templates directory }
BASE_DIR - main folder path
"""
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
"""

views.py

from django.shortcuts import render

def home(request):
    return render(request, "index.html") 

urls.py
path("",views.homePage)

#############################################################

# Passing data to HTML Pages using views
- create dictionary and pass it as parameter

views.py 

def Home(request):
    data = {
        'title':'Home Page',
        'pages':[12,22,334,5]
        'auther':[
            {'name':'ram', 'contect': 9734523454}
            {'name':'balram', 'contect': 9734523904}
        ]
    }
    return render(request, 'index.html', data)

- access parameter by {{ param }} on htmls

index.html
<title> {{title}} </title>

#############################################################

# looping in django

#index.html

{% for n in pages %}
<h1>{{forloop.counter}} pages are {{n}}</h1>
{% endfor%}

#dictionary accessing:

{% for a in auther %}
<tr> 
   <td>{{a.name}}</td>
   <td>{{a.contact}}</td>
</tr>
{% endfor %}

There are multiple method provided in for loops, 
refer documentation to check more.

#############################################################

# if else condition in django:

{% if pages|length < 0 %}
    <h1> Pages list not found </h1>
{% endif %}

{% for n in pages %}
<h1>{{forloop.counter}} pages are {{n}}</h1>
    {% if n < 60%}
    <h2> this book is small one</h2>
    {% endif %}
{% endfor%}

#############################################################

# Static folder in django 
Javascript, CSS, images etc

to access static folder add this line on settings.py

STATICFILES_DIRS = [
    BASE_DIR, 'static'
]

now u can change path while calling:

<link rel = "stylesheet" href="/static/css/style.css">
<img src="/static/images/logo.png"> 
ETC

#############################################################

# Header and footer in django : Incudes in django

create header & footer html files and add them into other pages :

header.html
navigation bar html code

footer.html
footer html code

index.html

{% include "header.html" %}
<body>

</body>
{% include "footer.html" %}

#############################################################

# Header & footer : extends in Django

base.html

{% include "header.html" %}
{% block content %}

{% endblock %}
{% include "footer.html" %}

index.html

{% extends 'base.html' %}

{% block content}
//body block html code
{% endblock}


############################################################

# load images etc from static

<!Doctype>
{% load static %}

<img src="{% static '/images/logo.png' %}" alt="">


##########################################################

# url template in django

urls.py

path("/about-us", view.aboutus, name='about')

header.html

<li class="nav-item">
    <a class="nav-link active" aria-current="page" href="{% url 'about' %}">About Us</a>
</li>

##########################################################

# if else condition with django

<nav class="{% if request.path == '/aboutus/' %} active {% endif %}>



##########################################################

# get method : 
The GET method sends the encoded user information appeneded to page request.
             the page and the information are separated by the ? character.

https://uloveanime.com:/index.html?key=value1&key2=value2

Restricted to send upto 1024 character only.

Never send GET method to send password or restricted data.

cannot used to send binary data, like image word doc etc.


Post Method : Transfer information via HTTP Header, the information is encoded as described
              in case.

Does not have any restricted on data size to be sent.

Can be used to send ASCII as well as binary data.

Secure HTTP.



##########################################################

# Django Forms:

create a froms.py inside APP.
# forms.py

from django import forms

class Usersform(forms.Form):
    num1 = forms.CharField()
    num2 = forms.CharField()

# views.py

from .form import Userform
def formValue():
    fn = Userform()
    data = {
        'form_key':fn
    }
    return render(request, 'userform.html', data)

# on html file 
{{form_key}}

##########################################################

Models in Django

first create app : python3 manage.py startapp service
service > models.py
# models.py

from django.db import models
class Service(models.Model):
    service_icon = models.CharField(max_length=60)
    service_title = models.CharField(max_length=100)
    service_desc = models.TextField()

settings.py from main folder

# settings.py

INSTALLED_APPS = [
    'service',
]

# Terminal

# python3 manage.py makemigrations
Migrations for 'services':
  services/migrations/0001_initial.py
    - Create model Service

# python3 manage.py migrate

Populate the table on admin or register on admin:

# admin.py

from django.contrib import admin
from .models import Service
class ServiceAdmin(admin.ModelAdmin):
    service_list = ('serv_icon', 'serv_title', 'serv_desc')

admin.site.register(Service, ServiceAdmin)

###################################################

# get data from models

# views.py

from service.models import Service

class HomePage(request):
    service_data = Service.objects.all()
    data ={
        'serviceData': service_data
    }
    return render(request, 'home.html', data)

# home.html
<div>
{% for item in serviceData %}
<h1> {{ item.service_icon }}</h1>
{% endfor %}
</div>

###################################################


# change admin password

python3 manage.py changepassword admin 

###################################################

# dynamic page redirecting

# views.py

def service(request, page_id):
    service_details = Service.objects.get(id=page_id)
    data = {

        'service_details': service_details
    }
    return render(request, 'service_page.html', data)

# urls.py

path('services/<page_id>', views.service, name='service')

# service_page.html

  <div class="container">
    <div class="row">
      <div class="col">
        <h1>{{ service_details.service_title }}</h1>
        <br>
        <p>{{ service_details.service_desc  }}</p>
      </div>
    </div> 
  </div>

###################################################

# adding media File on django :

Create a media folder on main folder

# setting.py
from os import path

MEDIA_URL = '/media/'
MEDIA_ROOT = path.join(BASE_DIR, 'media')


# urls.py
from django.conf import settings
from django.conf.urls.static import static

[at last]
if settings.DEBUG:
    urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

###################################################




