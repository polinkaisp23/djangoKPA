from django.shortcuts import render
from django.http import HttpResponse

def mainFunc(request):
    return HttpResponse('Главная функция главной страницы главного блока')
    