from django.db import models
from datetime import datetime, timedelta

# Create your models here.


class BookingForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    end_time = models.TimeField()
    guests = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        start_datetime = datetime.combine(self.date, self.time)
        end_datetime = start_datetime + timedelta(hours=2)
        self.end_time = end_datetime.time()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    table_capacity = models.IntegerField()
    is_reserved = models.BooleanField(default=False)
    reserved_by = models.ForeignKey(BookingForm, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"Table {self.table_number}"


class BookingAssignment(models.Model):
    booking = models.OneToOneField(BookingForm, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    assigned_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.booking.name} - {self.table.table_number}"