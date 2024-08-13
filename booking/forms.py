from django import forms
from .models import BookingForm
from django.utils import timezone
from datetime import time, timedelta
from datetime import datetime


def get_available_time_slots():
    # Generate time slots from 12 PM to 9 PM with 30 minutes interval
    start_time = time(12, 0)
    end_time = time(21, 0)
    time_slots = []

    current_time = start_time
    while current_time <= end_time:
        time_slots.append((current_time.strftime('%H:%M'), current_time.strftime('%H:%M')))
        current_time = (datetime.combine(datetime.today(), current_time) + timedelta(minutes=30)).time()

    return time_slots



class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingForm
        fields = ['name', 'email', 'phone', 'date', 'time']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'example@example.com'}),
            'phone': forms.TextInput(attrs={'placeholder': '+44 123 456 7890'}),
            'date': forms.DateInput(attrs={'type': 'date', 'value' : timezone.now().date()}),
            'time': forms.Select(choices=get_available_time_slots())
        }