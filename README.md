# Django
**Django Application**
1)	Start VsCode
2)	Set the virtual env. ( Python -m venv venv )
3)	Activate the venv Environment: 
Window: ./venv/Scripts/activate 
MAC: source venv/bin/activate
To Deactivate Run: deactivate
4)	Install Django (pip install django)
5)	Create a project using 
•	Django-admin startproject <project_name>
6)	Install mysql client
•	Pip install msqlclient
7)	 Change the settings.py file to connect to mysql
DATABASES = {
    	'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tutorial',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT':"3306"
    }
}

•	Install Xamp
•	Run apache server
•	Start server and mysql database
•	Create a database name that you mentioned in DATABASE settings

8)	Now run the server using command
	python manage.py runserver
	
9)	Creating an application
•	Python manage.py startapp <application_name>
10)	Create a template folder ()
11)	Create a static folder
12)	Create a urls.py file in application
13)	Register an application in setting.py in project folder
14)	In urls.py project folder link to the application urls using
		
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
	
15)	NOW CREATE A MODEL For example

from django.db import models
# Create your models here.
class Subscriber(models.Model):
    address_one = models.CharField(max_length=100)
    address_two = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    stripe_id = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name_plural = 'subscribers'

16)	Register your model in admins.py

from django.contrib import admin
from .models import Subscriber

# Register your models here.
admin.site.register(Subscriber)

17)	Now run the following command to make changes in database
•	Python manage.py makemigrations
•	Python manage.py migrate

18)	Create a input form in bootstrap HTML 
