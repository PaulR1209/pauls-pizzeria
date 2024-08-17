from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm, get_available_time_slots
from .models import Reservation, Table
from django.utils import timezone


def booking(request):
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

            for table in Table.objects.all():
                overlapping_reservations = Reservation.objects.filter(
                    table=table,
                    booking__date=date,
                    booking__time__lt=end_time,
                    booking__end_time__gt=start_time,
                )
                if (
                    not overlapping_reservations.exists()
                    and table.table_capacity >= booking.guests
                ):
                    available_table = table
                    break

            if available_table:
                booking_assignment = Reservation(booking=booking, table=available_table)
                booking_assignment.save()
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
        initial_data = {'email': request.user.email, 'name': request.user.username}
        form = BookingForm(initial=initial_data)

    return render(
        request,
        "booking/booking.html",
        {"form": form, "time_slots": get_available_time_slots()},
    )


def reservations(request):
    now = timezone.now()
    reservations = Reservation.objects.filter(
        booking__date__gte=now.date(),
    ).order_by("booking__date", "booking__time")

    return render(request, "booking/reservations.html", {"reservations": reservations})


def edit_reservation(request, reservation_id):

    reservation = get_object_or_404(Reservation, id=reservation_id)

    if request.method == "POST":
        form = BookingForm(request.POST, instance=reservation.booking)
        if form.is_valid():
            form.save()
            return redirect("reservations")

    else:
        form = BookingForm(instance=reservation.booking)

    return render(
        request,
        "booking/edit_reservation.html",
        {"reservation": reservation, "form": form},
    )


def cancel_reservation(request, reservation_id):

    reservation = get_object_or_404(Reservation, id=reservation_id)

    if request.method == "POST":
        reservation.delete()
        return redirect("reservations")

    return render(
        request, "booking/cancel_reservation.html", {"reservation": reservation}
    )
