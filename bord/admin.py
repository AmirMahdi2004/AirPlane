from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Airplane)
class AirplaneAdmin(admin.ModelAdmin):
    list_display = ('airplane_name',)


@admin.register(ServiceLifeLimited)
class ConditionsAdmin(admin.ModelAdmin):
    list_display = ('airplane',)


@admin.register(FltHrs)
class FltHrsAdmin(admin.ModelAdmin):
    list_display = ('airplane',)


@admin.register(MP)
class MPAdmin(admin.ModelAdmin):
    list_display = ('airplane',)


@admin.register(InputBord)
class InputBordAdmin(admin.ModelAdmin):
    list_display = ('airplane', 'date')
