from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookingForm, get_available_time_slots
from .models import Reservation, Table
from django.utils import timezone


def assign_table_and_save_booking(booking):
    """Assign a table to the booking if available and save it."""

    date = booking.date
    start_time = booking.time
    end_time = booking.end_time

    # Check if the booking date is Monday or Tuesday
    if booking.date.weekday() in [0, 1]:  # 0 is Monday, 1 is Tuesday
        raise ValueError("Sorry, we are closed on Mondays and Tuesdays.")

    # Find an available table
    available_table = None
    for table in Table.objects.all():
        overlapping_reservations = Reservation.objects.filter(
            table=table,
            booking__date=date,
            booking__time__lt=end_time,
            booking__end_time__gt=start_time,
        )
        # Check for overlapping reservations and if the table has enough capacity
        if (
            not overlapping_reservations.exists()
            and table.table_capacity >= booking.guests
        ):
            available_table = table
            break

    # If an available table is found, save the reservation
    if available_table:
        Reservation.objects.create(booking=booking, table=available_table)
        return available_table
    return None


def booking(request):
    """Handle booking requests."""
    if request.method == "POST":
        form = BookingForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()

            available_table = assign_table_and_save_booking(booking)
            # Check if a table was assigned
            if available_table:
                success_message = (
                    "Thank you for booking with us! We look forward to seeing you!"
                )
                return render(
                    request, "home.html", {"success_message": success_message}
                )
            else:
                form.add_error(
                    None,
                    "Sorry, we are fully booked at that time. Please try another time.",
                )
    else:
        initial_data = {"email": request.user.email, "name": request.user.username}
        form = BookingForm(initial=initial_data)

    return render(
        request,
        "booking/booking.html",
        {"form": form, "time_slots": get_available_time_slots()},
    )


def reservations(request):
    """Display the user's future reservations."""
    user = request.user
    now = timezone.now()
    reservations = Reservation.objects.filter(
        booking__user=user,
        booking__date__gte=now.date(),
    ).order_by("booking__date", "booking__time")

    return render(request, "booking/reservations.html", {"reservations": reservations})


def edit_reservation(request, reservation_id):
    """Allow users to update their reservation."""
    reservation = get_object_or_404(Reservation, id=reservation_id)

    # Check if the user is authorized to update the reservation
    if reservation.booking.user != request.user:
        return render(
            request,
            "home.html",
            {"error_message": "You are not authorized to update this reservation."},
        )

    if request.method == "POST":
        form = BookingForm(request.POST, instance=reservation.booking)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            # Delete the old reservation and assign a new table
            reservation.delete()
            available_table = assign_table_and_save_booking(booking)
            # Check if a table was assigned
            if available_table:
                success_message = "Your reservation has been updated successfully!"
                return render(
                    request, "home.html", {"success_message": success_message}
                )
            else:
                form.add_error(
                    None,
                    "Sorry, we are fully booked at that time. Please try another time.",
                )
    else:
        form = BookingForm(instance=reservation.booking)

    return render(
        request,
        "booking/booking.html",
        {
            "form": form,
            "time_slots": get_available_time_slots(),
            "is_edit": True,
        },
    )


def cancel_reservation(request, reservation_id):
    """Cancel a user's reservation."""
    reservation = get_object_or_404(Reservation, id=reservation_id)

    # Check if the user is authorized to cancel the reservation
    if reservation.booking.user != request.user:
        return render(
            request,
            "home.html",
            {"error_message": "You are not authorized to cancel this reservation."},
        )

    if request.method == "POST":
        reservation.delete()
        success_message = "Your reservation has been cancelled."
        return render(request, "home.html", {"success_message": success_message})

    return render(
        request, "booking/cancel_reservation.html", {"reservation": reservation}
    )
