from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('eventregister',views.eventregister,name="eventregister"),
    path('showallevent',views.showallevent,name="showallevent"),
    path('showoneevent/<str:id>',views.showoneevent,name="showoneevent"),
    path('deleteevent/<str:id>',views.deleteevent,name="showoneevent"),
]
