from django import forms
from .models import BookingForm
from django.utils import timezone
from datetime import time, timedelta, datetime
import pytz


def get_available_time_slots():
    # Generate time slots from 12 PM to 9 PM with 30 minutes interval
    start_time = time(12, 0)
    end_time = time(21, 0)
    time_slots = []
    current_time = start_time
    pytz.timezone('Europe/London')
    
    while current_time <= end_time:
        time_slots.append((current_time.strftime('%H:%M'), current_time.strftime('%H:%M')))
        current_time = (datetime.combine(datetime.today(), current_time) + timedelta(minutes=30)).time()

    return time_slots


class BookingForm(forms.ModelForm):

    def clean_time(self):
        chosen_date = self.cleaned_data.get('date')
        chosen_time = self.cleaned_data.get('time')
        if chosen_date and chosen_time:
            combined_datetime = datetime.combine(chosen_date, chosen_time)
            current_datetime = datetime.now()
            time_difference = combined_datetime - current_datetime
            if time_difference.total_seconds() < 0:
                raise forms.ValidationError("Please select a future time.")
            return chosen_time

    def clean_date(self):
        chosen_date = self.cleaned_data.get('date')
        if chosen_date:
            # Get the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
            day_of_week = chosen_date.weekday()
            if day_of_week in [0, 1]:  # Monday or Tuesday
                raise forms.ValidationError("We're closed on Mondays and Tuesdays.")
        return chosen_date

    class Meta:
        model = BookingForm
        fields = ['name', 'email', 'phone', 'date', 'time', 'guests']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'example@example.com'}),
            'phone': forms.TextInput(attrs={'placeholder': '+44 123 456 7890'}),
            'date': forms.DateInput(attrs={'type': 'date', 'value' : timezone.now().date(), 'min': timezone.now().date()}),
            'time': forms.Select(choices=get_available_time_slots()),
            'guests': forms.NumberInput(attrs={'placeholder': 'Max. Guests: 8', 'min': 1, 'max': 8})
        }