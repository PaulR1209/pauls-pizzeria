from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.booking), name='booking'),
    path('reservations/', login_required(views.reservations), name='reservations'),
]