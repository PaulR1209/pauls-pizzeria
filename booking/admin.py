from django.contrib import admin
from .models import BookingForm, Table, BookingAssignment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(BookingForm)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('name', 'date', 'time', 'guests', 'created_on')
    list_filter = ('date', 'time')
    search_fields = ['name', 'date', 'time', 'created_on']


@admin.register(Table)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('table_number', 'table_capacity', 'is_reserved', 'reserved_by')
    list_filter = ('table_number', 'table_capacity', 'is_reserved')
    search_fields = ['table_number', 'table_capacity', 'is_reserved', 'reserved_by']


@admin.register(BookingAssignment)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('name', 'date', 'time', 'guests', 'table', 'assigned_on')
    list_filter = ('date', 'time')
    search_fields = ['name', 'date', 'time', 'table', 'assigned_on']