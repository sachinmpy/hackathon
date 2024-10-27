from django.shortcuts import render, HttpResponse

# Create your views here.
def userprofile(request, username):
    return HttpResponse(f'User Profile {username}')

