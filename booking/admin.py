from django.contrib import admin
from .models import BookingForm
from django_summernote.admin import SummernoteModelAdmin

@admin.register(BookingForm)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('name', 'date', 'time', 'created_on')
    list_filter = ('date', 'time')
    search_fields = ['name', 'date', 'time', 'created_on']