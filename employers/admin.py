from django.contrib import admin
from .models import *
# Register your models here.


class EmployerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Employer, EmployerAdmin)
