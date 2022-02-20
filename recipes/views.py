from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request: HttpRequest):
    return HttpResponse('HOME!')


def sobre(request: HttpRequest):
    return HttpResponse('SOBRE!')


def contato(request: HttpRequest):
    return HttpResponse('CONTATO!')
