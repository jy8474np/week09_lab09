from django.urls import path
from . import views

urlpatterns = [
    path('', views.place_list, name='place_list'),
    path('about' , views.about , name='about')
]
