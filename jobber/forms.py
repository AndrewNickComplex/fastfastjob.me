from django.forms import forms, ModelForm, Textarea
from .models import Job, User, Category, Application, Jobber

class CreateJobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['title', 
        'description',
        'category', 
        'pay', 
        'number_of_positions',
        'address',
        'geolocation'
        ]

    