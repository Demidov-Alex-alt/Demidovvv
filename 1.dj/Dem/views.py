from django.shortcuts import render
from django.http import HttpResponse
from . import views

def index(request,name,age,interes):
    return HttpResponse(f'Меня зовут {name}.Мне {age}.Интересы:{interes}')


def about(request,city,eval):
    return HttpResponse(f'Я из{city}.Моя успеваемость {eval}.Я  люблю учиться')

def contacts(request):
    return HttpResponse('github https://github.com/Demidov-Alex-alt .telegram @Demidovvv')

