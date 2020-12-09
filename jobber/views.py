from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import Job, User, Tag

# Create your views here.
def listing(request):
    return render(request, "jobber/listing.html",{
        'jobs': Job.objects.all()
    })
    

# Designing "add to watchlist" page, make sure users cannot
# like jobs they made themselves.