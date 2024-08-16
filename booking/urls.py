from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.booking), name='booking'),
    path('mybookings/', login_required(views.mybookings), name='mybookings')
]