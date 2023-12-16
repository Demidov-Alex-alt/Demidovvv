from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    text = '<h1>Главная Страница<h1>' \
            '<p>my Информация</p>'
    return HttpResponse(text)


def about(request,name,work):
    return HttpResponse(f'О сайте.<br> Моё имя  {name}.<br> Я работаю  в {work}')

def contacts(request):
    return HttpResponse('Контакты')

