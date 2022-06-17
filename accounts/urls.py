# from django.conf.urls import url

from django.urls import include, path, re_path

from .views import *
from accounts.views import*
urlpatterns = [
     path('login/', loginview, name='login'),
     path('register/', registerview, name='register'),
     path('logout/', log_out, name="logout"),
    
     re_path(r'^(?P<username>.+)/$', profil, name='profile'),
]
