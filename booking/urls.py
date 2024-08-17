from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.booking), name='booking'),
    path('reservations/', login_required(views.reservations), name='reservations'),
    path('edit_reservation/<int:reservation_id>/', login_required(views.edit_reservation), name='edit_reservation'),
    path('cancel_reservation/<int:reservation_id>/', login_required(views.cancel_reservation), name='cancel_reservation'),
]