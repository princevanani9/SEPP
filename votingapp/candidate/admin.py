from django.contrib import admin
from .models import Candidate
# Register your models here.

@admin.register(Candidate)
class AdminCandidate(admin.ModelAdmin):
    pass