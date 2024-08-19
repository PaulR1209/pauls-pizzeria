from django.shortcuts import render
from .forms import Contact

# Create your views here.


def contact(request):
    # Check if the form is valid and save the data
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            form.save()
            success_message = (
                "Thank you for contacting us! We will be in touch shortly.")
            return render(request, 'home.html', {
                'success_message': success_message})
    # Check if the user is authenticated and pre-fill the form
    else:
        if request.user.is_authenticated:
            form = Contact(initial={
                'email': request.user.email, 'name': request.user.username})
        else:
            form = Contact()

    return render(request, 'contact/contact.html', {'form': form})
