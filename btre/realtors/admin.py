from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Realtor)
class Realtor(admin.ModelAdmin):
    list_display=('id','name','email','hire_date')
    list_display_links=('id','name')
    search_fields=('name',)
    list_per_page=20
    
# admin.site.register(Realtor)