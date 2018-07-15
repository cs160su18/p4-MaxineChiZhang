# chat/urls.py
from django.conf.urls import url

from . import views

from django.urls import path

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
    
#     path('fitting/',views.c, name='fitting'),
    url(r'^fitting/$', views.fitting, name='fitting')
]

