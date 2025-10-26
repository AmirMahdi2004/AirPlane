from django import forms
from django.forms.widgets import Input

from .models import *


class SLLForm(forms.ModelForm):
    class Meta:
        model = ServiceLifeLimited
        fields = '__all__'


class MpForm(forms.ModelForm):
    class Meta:
        model = MP
        fields = '__all__'


class FltHrsForm(forms.ModelForm):
    class Meta:
        model = FltHrs
        fields = '__all__'


class InputBordForm(forms.ModelForm):
    class Meta:
        model = InputBord
        fields = ['airplane', 'AircraftFlightHours', 'AircraftCycles', 'Landings']
