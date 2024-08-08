from django import forms
from .models import Contact
from phonenumber_field.formfields import PhoneNumberField


class Contact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'example@example.com'}),
            'phone': forms.TextInput(attrs={'placeholder': '+44 123 456 7890'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Enter a title for your message'}),
            'message': forms.Textarea(attrs={'placeholder': 'Type your message here'}),
        }