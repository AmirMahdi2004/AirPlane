from django.contrib.auth.forms import AdminUserCreationForm, UserChangeForm, UserCreationForm
from django import forms
from .models import CustomUser, SupportTicket, RequestRegister


class CustomUserCreationForm(AdminUserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'role', 'manager', 'personnel_code', 'phone_number', 'Working_hours',
                  'is_active', 'is_staff')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'personnel_code', 'phone_number', 'Working_hours',
                  'is_active', 'is_staff')


class CreateUserFrom(UserCreationForm):
    password1 = forms.CharField(max_length=20, widget=forms.PasswordInput, label='password')
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput, label='repeat password')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'role', 'manager', 'personnel_code', 'phone_number', 'is_active', 'is_staff')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = "admin"
        if commit:
            user.save()
        return user


class SupportTicketForm(forms.ModelForm):
    class Meta:
        model = SupportTicket
        fields = ['title', 'system_id', 'priority', 'ticket_type', 'description']


class RequestRegisterForm(forms.ModelForm):
    class Meta:
        model = RequestRegister
        fields = ['company_name', 'phone_number', 'email','date_of_birth']
