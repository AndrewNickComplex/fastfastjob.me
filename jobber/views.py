from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import Job, User, Category, Application, Jobber
from .forms import CreateJobForm
from django.contrib import messages

# Create your views here.
def listing(request):
    return render(request, "jobber/listing.html",{
        'jobs': Job.objects.all(), 'categories': Category.objects.all()
    })
    
def create_job(request):
    if not request.user.is_authenticated:
        messages.info(request, "Please login first")
        return HttpResponseRedirect(reverse('login'))
    
    if request.method == "POST":
        by = User.objects.get(username=request.user.username)
        title = request.POST["title"]
        description = request.POST["description"]
        category = Category.objects.get(pk=request.POST["category"])
        pay = request.POST["pay"]
        number_of_positions = request.POST["number_of_positions"]
        #To include geolocation for google maps api binding
        #geolocation = request.POST["geolocation"]
        address = request.POST["address"]

        job = Job(created_by=by,title=title,description=description,category=category,pay=pay,
        number_of_positions=number_of_positions,address=address)
        job.save()
        #return to the page of the job that was created
        url = reverse('job', kwargs={'job_id': job.pk})
        return HttpResponseRedirect(url)

    else:
        return render(request, "jobber/createjob.html",{
            "form": CreateJobForm,
            'categories': Category.objects.all()
        })


def login_view(request):    
    if request.method == "POST":
        #if user already signed in, return them to listing page.
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('listing'))
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("listing"))
        else:
            return render(request, "jobber/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "jobber/login.html",{'categories': Category.objects.all()})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("listing"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "jobber/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, password)
            user.save()
        except IntegrityError:
            return render(request, "jobber/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("listing"))
    else:
        return render(request, "jobber/register.html",{'categories': Category.objects.all()})


def job(request, job_id):
    is_user = request.user.is_authenticated
    try:
        job = Job.objects.get(pk=job_id)
    except:
        messages.error(request, "Job not found")
        return HttpResponseRedirect(reverse('listing'))

    return render(request, "jobber/job.html",{
        "job":job, "is_user": is_user, 'categories': Category.objects.all()
    })

# What to do if someone applies for job? 
# Redirect to whatsapp/email/starts chat in app??
def application(request):
    pass

def user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        jobs_posted = Job.objects.filter(created_by=user)
    except:
        messages.error(request, "User not found")
        return HttpResponseRedirect(reverse('listing'))
    
    return render(request, "jobber/user.html", {
        "user": user,
        "jobs_posted": jobs_posted,
        'categories': Category.objects.all()
    })

def category(request, category_name):
    #Get category object
    try:
        category = Category.objects.get(title=category_name)
    except: 
        messages.error(request, f"The Category ({category_name}) is not found")
        return HttpResponseRedirect(reverse('listing'))
    #Get jobs listed under category
    #?? Get it using category name or id??
    jobs = Job.objects.filter(category=category)
    if jobs.count() == 0:
        messages.error(request, f"There are no jobs under {category} presently") 
        return HttpResponseRedirect(reverse('listing'))

    return render(request, "jobber/categorylisting.html", {
        "jobs": jobs, 
        "category_name": category_name,
        'categories': Category.objects.all()
    })
    
