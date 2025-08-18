from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('employee', 'Employee'),
    ]
    WORK_SHIFT_CHOICES = [
        ('NightShift', 'NightShift'),
        ('MorningShift', 'MorningShift'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='admin')
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subordinates')
    personnel_code = models.CharField(max_length=10, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    Working_hours = models.CharField(choices=WORK_SHIFT_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.username


class SupportTicket(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'کم'),
        ('medium', 'متوسط'),
        ('high', 'بالا'),
    ]

    TICKET_TYPE_CHOICES = [
        ('airplane_registration', 'ثبت‌نام هواپیما'),
        ('support', 'پشتیبانی'),
        ('financial', 'مالی'),
        ('remote_connection', 'اتصال از راه دور'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    system_id = models.CharField(max_length=100)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    ticket_type = models.CharField(max_length=30, choices=TICKET_TYPE_CHOICES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class RequestRegister(models.Model):
    company_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField()
    date_of_birth = models.DateField()

    def __str__(self):
        return self.company_name
