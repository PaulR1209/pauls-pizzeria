from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User

# Create your models here.


# BookingForm model
class BookingForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    end_time = models.TimeField()
    guests = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    # Save the end time of the booking
    def save(self, *args, **kwargs):
        start_datetime = datetime.combine(self.date, self.time)
        end_datetime = start_datetime + timedelta(hours=2)
        self.end_time = end_datetime.time()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# Table model
class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    table_capacity = models.IntegerField()

    def __str__(self):
        return f"Table {self.table_number}"


# Reservation model to assign a booking to a table
class Reservation(models.Model):
    booking = models.OneToOneField(BookingForm, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    assigned_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.booking.name} - {self.table.table_number}"
