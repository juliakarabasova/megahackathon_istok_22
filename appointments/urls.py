from django.urls import path
from . import views

urlpatterns = [
    path('', views.appointment_list, name='appointment_list'),
    path('create/', views.appointment_create, name='appointment_create'),
    path('contact/', views.contact, name='contact'),
    path('save-appointment/', views.save_appointment, name='save_appointment'),
]
