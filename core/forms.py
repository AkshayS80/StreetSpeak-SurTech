from django import forms
from django.core.validators import RegexValidator
from .models import Report

class ReportForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        validators=[RegexValidator(r'^[A-Za-z\s]+$', 'Only letters are allowed.')]
    )
    phone = forms.CharField(
        validators=[RegexValidator(r'^\+91[6-9]\d{9}$', 'Enter a valid Indian phone number starting with +91')]
    )

    class Meta:
        model = Report
        fields = ['name', 'phone', 'location', 'description', 'image']
