# Create_Django_Project_IOS

Create a new Project

Create Folder

Create Github Repo

Follow Repo Instruction and create a README.MD

Create a Virtual Environment at Root of Project

virtualenv -p python3 djangoPy3Env

Activate Environment

source djangoPy3Env/bin/activate

Install Django

Pip install Django==1.10

Verify Installation

pip list

Create New Project ( replace {new_proj} with a valid name )

django-admin startproject {new_proj}

Move to new path

cd {new_proj}

Test Server

python manage.py runserver

Go to Browser and enter URL localhost:8000

Exit Server

control c

Create Apps Folder

mkdir apps

Move to new path

cd apps

Create File Structure in apps ( replace {new_app} with a valid name )

python ../manage.py startapp {new_app}

Create file urls.py

touch urls.py

EDIT 4 FILES

1. {project_name}\{project_name}\settings.py

`INSTALLED_APPS = [
       'apps.{your_app_name_here}', # create this line with your app's name
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
   ]
`
2. {project_name}\{project_name}\urls.py

`from django.conf.urls import url, include			# add include 
  # from django.contrib import admin             		# comment out, or just delete

  urlpatterns = [
    url(r'^', include('apps.{your_app_name_here}.urls')),	# use your app name here
    # url(r'^admin/', admin.sites.urls)         		                # comment out, or just delete
  ]
`

3. {project_name}\apps\{app_name}\urls.py

`## {app_name} ##
  from django.conf.urls import url
  from . import views
                    
  urlpatterns = [
      url(r'^$', views.index),
  ]
`

4. {project_name}\apps\{app_name}\views.py

`## {app name} ##
  from django.shortcuts import render, HttpResponse

  def index(request):
      return HttpResponse("this is the equivalent of @app.route('/')!")
      Or
      context = {}
      return render(request, “{new_app}/index.html”, context)

If using index.html

Run Migrations at Root of Project

python manage.py migrate

Create templates folder under {new_app}

Create {new_app} folder under templates folder

Create index.html under {new_app} folder

Create static folder under {new_app}

Create {new_app}folder under static folder

Create css \ js \ images folders under {new_app} folder

Create style.css \ script.js \ *.png’s in corresponding folders

Add the following too index.html

{% load static %}
 <link rel="stylesheet" href="{% static 'new_app/css/style.css' %}">   

Return to root of project

cd ../..

Test Server

python manage.py runserver

.git add .
.git commit -m “server running”
.git push





 