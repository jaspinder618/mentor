from django import forms
from django.contrib.admin.widgets import AdminTimeWidget


class CustomTimeField(forms.TimeField):
    widget = AdminTimeWidget(attrs={'class': 'vTimeField'})
