from django.contrib import admin
from committee.models import Applicant, Committeeman, Info

# Register your models here.

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    pass

@admin.register(Committeeman)
class CommitteemanAdmin(admin.ModelAdmin):
    pass

@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    pass
