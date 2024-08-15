from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BookingForm, Table, BookingAssignment
from .forms import BookingForm

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            
            # Find an available table
            available_table = Table.objects.filter(is_reserved=False, table_capacity__gte=booking.guests).first()
            
            if available_table:
                # Reserve the table
                available_table.is_reserved = True
                available_table.reserved_by = booking
                available_table.save()
                
                # Create a booking assignment
                BookingAssignment.objects.create(booking=booking, table=available_table)
                
                return HttpResponse("Booking successful! Table assigned.")
            else:
                return HttpResponse("No available tables for the selected time.")
    else:
        form = BookingForm()
    print('Rendering booking form')
    return render(request, 'booking/booking.html', {'form': form})