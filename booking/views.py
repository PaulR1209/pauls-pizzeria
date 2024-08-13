from django.shortcuts import render
from .forms import BookingForm


# Create your views here.

def booking(request):

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            booking_message = "Thank you for booking with us! We look forward to seeing you soon."
            return render(request, 'home.html', {'booking_message': booking_message})
    else:
        form = BookingForm(initial={'email': request.user.email})

    return render(request, 'booking/booking.html', {'form': form})