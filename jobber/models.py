from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# from phonenumber_field.modelfields import PhoneNumberField
from django_google_maps import fields as map_fields
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

class Tag(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.title}"

class Job(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey('User', null=False, on_delete=models.CASCADE, related_name="jobs_created")
    title = models.CharField(max_length=60)
    #address and geo location both uses the django_google_maps package
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)
    description = models.TextField(blank=True,max_length=2000)
    # location: How will the GMaps/GeoDjango API access and provide this?
    # just going to be saved as longtitude and latitude
    tag = models.ForeignKey(Tag, null=False, on_delete=models.CASCADE, related_name="jobs")
    created_at = models.DateTimeField(default=timezone.now)
    estimate_pay = models.DecimalField(decimal_places=2, max_digits=7)
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
    # PhoneNumberField is from https://pypi.org/project/django-phonenumber-field/
    #Issue #11: contact_number = models.PhoneNumberField()
    gender = models.CharField(choices=gender, blank=False, max_length = 10)
    created_at = models.DateTimeField(default=timezone.now)
    #Watchlist for jobs that a jobber stores in joblist.
    jobs_interested = models.ForeignKey(Job, null = True, blank=True, on_delete=models.CASCADE, related_name='interested_by')
    def __str__(self):
        return f"{self.id}: {self.username} ({self.first_name} {self.last_name} )"

    #for django tests if user is valid
    def is_valid_user(self):
        pass
