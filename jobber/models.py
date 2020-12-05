from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from phonenumber_field.models import PhoneNumberField
# Create your models here.

method = (
    ('whatsapp','whatsapp'),
    ('email','email'),
    ('phone','phone'),
    ('facebook','facebook')
)

class User(AbstractUser):
    #Abstract User class inherits username, password, email, etc
    pk = models.AutoField(primary_key=True)
    contact_method = models.CharField(choices = method, max_length = 30)
    # Phone Number Field is from https://github.com/stefanfoulis/django-phonenumber-field
    contact_number = models.PhoneNumberField()
    #Watchlist for jobs that a jobber stores in joblist.
    jobs_interested = models.ForeignKey(Job, null = True, on_delete=models.CASCADE)
    #The list of jobs that a boss user posted
    jobs_posted = models.ForeignKey(Job, null = True, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.id}: {self.username} @ {self.email}"

def Job(models.Model):
    pk = models.AutoField(primary_key=True)
    listed_by = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=2000)
    # location: How will the GMaps/GeoDjango API access and provide this?
    tag = models.ForeignKey(Tag, null=False, on_delete=models.CASCADE, related_name="jobs")
    created_at = models.DateTimeField(default=timezone.now)
    estimate_pay = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return f"{self.pk}: {self.title} by {self.listed_by}"

def Tag(models.Model):
    title = models.CharField(max_length=30)