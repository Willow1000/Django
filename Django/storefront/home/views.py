from django.shortcuts import render
from django.http import HttpResponse

def say_welcome(request):
    return HttpResponse("wELCOME TO THE HOMEPAGE")
# Create your views here.
