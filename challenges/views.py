from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def january(request):
    return HttpResponse("Eat only meet for the entire month")


def february(request):
    return HttpResponse("Work out for 30 minutes each day")
