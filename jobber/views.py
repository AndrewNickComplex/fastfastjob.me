from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

# Create your views here.
def listing(request):
    return HttpResponse('Welcome to Jobber!')