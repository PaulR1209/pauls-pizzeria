from django.shortcuts import render
from .forms import Contact

# Create your views here.

def contact(request):

    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Contact()

    return render(request, 'contact/contact.html', {'form': form})