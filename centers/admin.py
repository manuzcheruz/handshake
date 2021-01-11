from django.contrib import admin
from .models import *
# Register your models here.


class CenterAdmin(admin.ModelAdmin):
    pass

admin.site.register(Center, CenterAdmin)
