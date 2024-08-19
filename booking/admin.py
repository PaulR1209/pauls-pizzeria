from django.contrib import admin
from .models import BookingForm, Table, Reservation
from django_summernote.admin import SummernoteModelAdmin


@admin.register(BookingForm)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('name', 'date', 'time', 'guests', 'created_on')
    list_filter = ('date',)
    search_fields = ['name', 'date', 'time', 'created_on']


@admin.register(Table)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('table_number', 'table_capacity')
    list_filter = ('table_capacity',)
    search_fields = ['table_number', 'table_capacity']


@admin.register(Reservation)
class ReservationAdmin(SummernoteModelAdmin):

    list_display = ('booking', 'table', 'booking_time', 'booking_date')
    list_filter = ('assigned_on', 'booking__date')
    search_fields = ['booking__name', 'table__table_number', 'booking__date']
    ordering = ('booking__time',)

    def booking_time(self, obj):
        return obj.booking.time

    def booking_date(self, obj):
        return obj.booking.date
