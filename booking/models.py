from django.db import models

# Create your models here.


class BookingForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name