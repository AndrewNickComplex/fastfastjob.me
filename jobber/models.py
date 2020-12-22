from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django_google_maps import fields as map_fields
from phone_field import PhoneField


# Create your models here.

#contact methods for User to choose preferred method of contact from
method = (
    ('whatsapp','whatsapp'),
    ('email','email'),
    ('phone','phone'),
    ('facebook','facebook')
)

gender = (
    ('male','male'),
    ('female','female'),
    ('others','others')
)

class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.title}"

class Job(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey('User', null=False, on_delete=models.CASCADE, related_name="jobs_created")
    title = models.CharField(max_length=60, blank=False)
    #address and geo location both uses the django_google_maps package
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)
    description = models.TextField(blank=True,max_length=2000)
    category = models.ForeignKey(Category, null=False, on_delete=models.CASCADE, related_name="jobs")
    created_at = models.DateTimeField(default=timezone.now)
    pay = models.DecimalField(decimal_places=2, max_digits=7, blank=False)
    number_of_positions = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.title} by {self.created_by}"

    #for django tests if job is valid
    def is_valid_job(self):
        pass

class User(AbstractUser):
    #Abstract User class inherits username, password, email, etc
    id = models.AutoField(primary_key=True)
    #address and geo location both uses the django_google_maps package
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)
    contact_method = models.CharField(choices = method, max_length = 30)
    # PhoneNumberField is from https://pypi.org/project/django-phone-field/
    phone = PhoneField(blank=True, help_text='Contact phone number')
    gender = models.CharField(choices=gender, blank=False, max_length = 10)
    created_at = models.DateTimeField(default=timezone.now)
    #Watchlist for jobs that a jobber stores in joblist.
    jobs_interested = models.ForeignKey(Job, null = True, blank=True, on_delete=models.CASCADE, related_name='interested_by')
    def __str__(self):
        return f"{self.id}: {self.username} ({self.first_name} {self.last_name} )"

    #for django tests if user is valid
    def is_valid_user(self):
        pass

class Application(models.Model):
    id = models.AutoField(primary_key=True)
    date_applied = models.DateTimeField(default=timezone.now)
    by = models.ForeignKey(User, null = False, on_delete=models.CASCADE, related_name="applications")
    job = models.ForeignKey(Job, null=False, on_delete=models.CASCADE, related_name="applications")
    is_closed = models.BooleanField(default=False, blank=False)

#For jobbers to have a profile, where we notify them if there's 
#jobs they're interested in appearing via their preferred
#contact method
class Jobber(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    interest = models.ForeignKey(Category, null=True,on_delete=models.CASCADE)
    description = models.TextField(max_length=3000, blank=True)
