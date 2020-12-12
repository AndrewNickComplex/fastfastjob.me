from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from .models import Job, User, Category, Application, Jobber


# Register your models here.
class Admin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }

admin.site.register(Job)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Application)
admin.site.register(Jobber)