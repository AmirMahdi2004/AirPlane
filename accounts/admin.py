# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'role', 'manager', 'is_staff', 'is_active', 'phone_number', 'Working_hours',
                    'personnel_code')
    list_filter = ('role', 'is_active', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('username',)
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'manager', 'phone_number', 'Working_hours', 'personnel_code')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'manager', 'phone_number', 'Working_hours', 'personnel_code')}),
    )


class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'ticket_type', 'priority', 'created_at', 'user')
    search_fields = ('title', 'system_id', 'description')
    list_filter = ('priority', 'ticket_type')
    date_hierarchy = 'created_at'
    fieldsets = (
        ('اطلاعات تیکت', {
            'fields': ('title', 'system_id', 'description')
        }),
        ('اطلاعات اولویت و نوع', {
            'fields': ('priority', 'ticket_type', 'user')
        }),
    )


class RequestRegisterAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'phone_number')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(SupportTicket, SupportTicketAdmin)
admin.site.register(RequestRegister, RequestRegisterAdmin)
