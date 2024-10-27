from django.shortcuts import render, HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse('This is index page')


def login(request):
    return HttpResponse('Login Page')


def register(request):
    return HttpResponse('Registration Page')


def logout(request):
    return HttpResponse("HANDLE THIS!!!!")
