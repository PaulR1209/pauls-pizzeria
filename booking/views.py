from django.shortcuts import render
from .forms import BookingForm, get_available_time_slots
from .models import Reservation, Table


def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            date = booking.date
            start_time = booking.time
            end_time = booking.end_time

            available_table = None

            for table in Table.objects.all():
                overlapping_reservations = Reservation.objects.filter(
                    table=table,
                    booking__date=date,
                    booking__time__lt=end_time,
                    booking__end_time__gt=start_time
                )
                if not overlapping_reservations.exists() and table.table_capacity >= booking.guests:
                    available_table = table
                    break

            if available_table:
                booking_assignment = Reservation(booking=booking, table=available_table)
                booking_assignment.save()
                success_message = 'Thank you for booking with us! We look forward to seeing you!'
                return render(request, 'home.html', {'success_message': success_message})
            else:
                form.add_error(None, "Sorry, we are fully booked at that time. Please try another time.")
    else:
        form = BookingForm()

    return render(request, 'booking/booking.html', {'form': form, 'time_slots': get_available_time_slots()})