from django.contrib import admin
from profiles_api import models

# Register your models here.
#This line registers UserProfile to be accesed through the admin side
admin.site.register(models.UserProfile)
