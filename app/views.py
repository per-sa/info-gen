from http.client import HTTPResponse
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello, world. Response.")
