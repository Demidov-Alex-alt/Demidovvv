from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.index, name='home',kwargs = {'name':'Демидов Александр ','age':'16','interes':'Учеба'}),
    path('about',views.about,name = 'about',kwargs = {'city':'Оренбург','eval':'Отличная'}),
    path('contacts', views.contacts, name='contacts'),

]
