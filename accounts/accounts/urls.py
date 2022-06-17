# from django.conf.urls import url

from django.urls import include, path, re_path

from .views import *

urlpatterns = [
     re_path('login/', loginview, name='login'),
     re_path('register/', registerview, name='register'),
     re_path('logout/', log_out, name="logout"),
     re_path(r'^(?P<username>.+)/$', profil, name='profile'),
]
