from django.contrib import admin
from .models import *
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Student, StudentAdmin)
