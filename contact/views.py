from django.shortcuts import render
from .forms import Contact

# Create your views here.

def submit(request):
    return render(request, 'contact/submit.html')

def contact(request):

    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            form.save()
            success_message = "Thank you for contacting us, we will get in touch shortly"
            return render(request, 'contact/submit.html', {'success_message': success_message})
    else:
        form = Contact()

    return render(request, 'contact/contact.html', {'form': form})