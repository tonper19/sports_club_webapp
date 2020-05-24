from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'a001_main/index.html')


def signin(request):
    return render(request, 'a001_main/signin.html')
