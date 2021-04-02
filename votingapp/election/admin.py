from django.contrib import admin
from .models import CreateElection

@admin.register(CreateElection)
class AdminCreateElecion(admin.ModelAdmin):
    list_display = ['name','type']

# Register your models here.
