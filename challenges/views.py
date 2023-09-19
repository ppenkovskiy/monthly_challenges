from django.shortcuts import render
from django.http import HttpResponse


def index_1(request):
    return HttpResponse('This works!')


def index_2(request):
    return HttpResponse('This also works!')
