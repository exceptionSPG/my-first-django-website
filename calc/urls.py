from os import name
from django.urls import path,include
from django.urls.conf import include

from.import views

urlpatterns = [
    path('', views.home,name='home'),
    path('add', views.add, name='add')
]