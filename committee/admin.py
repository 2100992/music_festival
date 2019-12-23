from codecs import register
from django.contrib import admin
from committee.models import Applicant, Committeeman

# Register your models here.

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    pass

@admin.register(Committeeman)
class CommitteemanAdmin(admin.ModelAdmin):
    pass
