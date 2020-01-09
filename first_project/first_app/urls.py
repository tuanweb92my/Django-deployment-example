from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from first_app import views
from django.conf.urls import include

urlpatterns = [
    path('',views.index,name='index'),
    url(r'^$',views.index,name='index')

]
