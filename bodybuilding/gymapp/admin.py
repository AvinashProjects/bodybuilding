from django.contrib import admin
from gymapp.models import *
# Register your models here.

class AdminMember(admin.ModelAdmin):
    list_display = ['name','phone','plan','email']

class AdminPlan(admin.ModelAdmin):
    list_display = ['name','amount','duration']

admin.site.register(Member,AdminMember)
admin.site.register(Plan,AdminPlan)
