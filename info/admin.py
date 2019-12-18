from codecs import register
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Info, Participant, Gallery, Location

# Register your models here.

@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    pass