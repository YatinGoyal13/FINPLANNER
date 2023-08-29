from django.contrib import admin
from django.http import HttpResponse
from .models import Profile


admin.site.register(Profile)