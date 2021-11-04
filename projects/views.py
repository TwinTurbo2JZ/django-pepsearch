from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def projects(response):
    return HttpResponse('getting a response back from the function')

def project(response, pk):
    return HttpResponse('is a single project, and the value is' + ' ' + str(pk))