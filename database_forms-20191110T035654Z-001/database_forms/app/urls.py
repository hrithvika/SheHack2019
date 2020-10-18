from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.createpost, name='create'),
    path('forms/', views.forms, name='forms'),
    path('mahadiscom/', views.mahadiscomf, name='mahadiscomf'),
    path('indoor/', views.myview, name='my_view_name'),
    path('outdoor/', views.myoutview, name='my_out_view_name'),
    path('food/', views.food, name='food'),
    path('shopping/', views.shopping, name='shopping'),
    path('car/', views.car, name='car'),
    path('scooter/', views.scooter, name='scooter'),
    path('cab/', views.cab, name='cab'),
    path('rickshaw/', views.rickshaw, name='rickshaw'),
    path('bus/', views.bus, name='bus'),
    path('cycle/', views.cycle, name='cycle'),
    path('walking/', views.walking, name='walking'),
    path('train/', views.train, name='train'),
    path('flight/', views.flight, name='flight'),
    path('earth/', views.earth, name='earth'),
    path('endride/', views.endride, name='endride'),
    path('output/', views.output,name='output'),
    path('statistics/', views.statistics, name='statistics'),
    path('solar/', views.solar, name='solar')
]
