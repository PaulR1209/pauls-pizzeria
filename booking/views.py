from django.shortcuts import render
from .forms import BookingForm, get_available_time_slots
from .models import BookingAssignment, Table


def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            table = Table.objects.filter(is_reserved=False, table_capacity__gte=booking.guests).first()
            if table:
                end_time = booking.end_time
                booking_assignment = BookingAssignment(booking=booking, table=table)
                booking_assignment.save()
                table.is_reserved = True
                table.reserved_by = booking
                table.save()
                success_message = 'Thank you for booking with us! We look forward to seeing you!'
                return render(request, 'home.html', {'success_message': success_message})
            else:
                form.add_error(None, "Sorry, we are fully booked at that time. Please try another time.")
    else:
        form = BookingForm()

    return render(request, 'booking/booking.html', {'form': form, 'time_slots': get_available_time_slots()})