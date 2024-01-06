from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    return HttpResponse('hi world')

def home(request):
    return HttpResponse('my page')
