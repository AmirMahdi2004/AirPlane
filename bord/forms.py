from django import forms
from.models import FltHrs


class FltHrsForm(forms.ModelForm):
    class Meta:
        model = FltHrs
        fields = '__all__'

