from django.contrib import admin
from .models import Contact
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Contact)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('name', 'subject', 'created_on')
    search_fields = ['name', 'subject', 'created_on']