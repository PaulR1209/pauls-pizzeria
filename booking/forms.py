from django import forms
from .models import BookingForm
from django.utils import timezone



class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingForm
        fields = ['name', 'email', 'phone', 'date', 'time']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'example@example.com'}),
            'phone': forms.TextInput(attrs={'placeholder': '+44 123 456 7890'}),
            'date': forms.DateInput(attrs={'type': 'date', 'value' : timezone.now().date()}),
            'time': forms.TimeInput(attrs={'type': 'time', 'value' : timezone.now().time()}),
        }