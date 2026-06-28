from django.urls import path
from .views import *

urlpatterns = [
    path('', landing_page, name='home'),
    path('about/', about_page, name='about'),
]

  