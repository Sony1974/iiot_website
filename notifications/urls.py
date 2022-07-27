
from django.urls import path
from . import views

urlpatterns = [
    path('notif_form/', views.notif_form, name='notif_form'),
]