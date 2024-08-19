from django.shortcuts import render, get_object_or_404
from .forms import BookingForm, get_available_time_slots
from .models import Reservation, Table
from django.utils import timezone


def booking(request):
    # Check if booking form is valid and save the booking
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking = form.save()
            date = booking.date
            start_time = booking.time
            end_time = booking.end_time

            available_table = None
            # Check if there is a table available for the booking
            for table in Table.objects.all():
                overlapping_reservations = Reservation.objects.filter(
                    table=table,
                    booking__date=date,
                    booking__time__lt=end_time,
                    booking__end_time__gt=start_time,
                )
                # Check if there are no overlapping reservations and
                # if the table has enough capacity
                if (
                    not overlapping_reservations.exists()
                    and table.table_capacity >= booking.guests
                ):
                    available_table = table
                    break
            # If there is an available table, assign the booking to the table
            if available_table:
                booking_assignment = Reservation(
                    booking=booking, table=available_table)
                booking_assignment.save()
                success_message = (
                    "Thank you for booking with us!"
                    " We look forward to seeing you!"
                )
                return render(
                    request, "home.html", {"success_message": success_message}
                )
            # If there are no available tables, display an error message
            else:
                form.add_error(
                    None,
                    "Sorry, we are fully booked at that time."
                    " Please try another time.",
                )
    # If the form is not valid,
    # render the form again with user email and name pre-filled
    else:
        initial_data = {
            'email': request.user.email, 'name': request.user.username}
        form = BookingForm(initial=initial_data)
    # Render the booking form with available time slots
    return render(
        request,
        "booking/booking.html",
        {"form": form, "time_slots": get_available_time_slots()},
    )


def reservations(request):
    # Get all reservations that are in the future
    now = timezone.now()
    reservations = Reservation.objects.filter(
        booking__date__gte=now.date(),
    ).order_by("booking__date", "booking__time")
    # Render the reservations page with the reservations
    return render(
        request, "booking/reservations.html", {"reservations": reservations})


def edit_reservation(request, reservation_id):
    # Get the reservation to edit
    reservation = get_object_or_404(Reservation, id=reservation_id)
    # Check if the form is valid and save the booking
    if request.method == "POST":
        form = BookingForm(request.POST, instance=reservation.booking)
        if form.is_valid():
            form.save()
            edit_message = "Your reservation has been updated."
            return render(request, "home.html", {"edit_message": edit_message})
    # If the form is not valid, render the form again
    else:
        form = BookingForm(instance=reservation.booking)
    # Render the edit reservation form
    return render(
        request,
        "booking/edit_reservation.html",
        {"reservation": reservation, "form": form},
    )


def cancel_reservation(request, reservation_id):
    # Get the reservation to cancel
    reservation = get_object_or_404(Reservation, id=reservation_id)
    # Check if the user confirms the cancellation
    if request.method == "POST":
        reservation.delete()
        cancel_message = "Your reservation has been cancelled."
        return render(request, "home.html", {"cancel_message": cancel_message})
    # Render the cancel reservation page
    return render(
        request, "booking/cancel_reservation.html", {
            "reservation": reservation}
    )
