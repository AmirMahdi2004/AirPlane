from django import forms
from django.forms.widgets import Input

from .models import FltHrs, InputBord


class FltHrsForm(forms.ModelForm):
    class Meta:
        model = FltHrs
        fields = '__all__'


class InputBordForm(forms.ModelForm):
    class Meta:
        model = InputBord
        fields = ['airplane','AircraftFlightHours', 'AircraftCycles', 'Landings']
