from django.forms import forms, ModelForm, Textarea
from django import forms
from .models import Job, User, Category, Application, Jobber

class CreateJobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['title', 
        'description',
        'category', 
        'pay', 
        'number_of_positions',
        'address'
        ]

        #styling through bootstrap class in form-control
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Describe the job in 3-5 sentences."}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'pay': forms.TextInput(attrs={'class': 'form-control'}),
            'number_of_positions': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            
        }

    