from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.http import require_POST

from .forms import AppointmentForm, ContactForm
from .models import Appointment


@login_required
def appointment_list(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'appointments/appointment_list.html', {'appointments': appointments})


@login_required
def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            messages.success(request, 'Запись успешно создана!')
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/appointment_form.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            interest = form.cleaned_data['interest']
            phone_number = form.cleaned_data['phone_number']
            contact_method = form.cleaned_data['contact_method']

            message = f'Интересы: {", ".join(interest)}\nНомер телефона: {phone_number}\nСпособ связи: {contact_method}'

            send_mail(
                f'Сообщение от {name}',
                message,
                email,
                ['recipient@example.com'],  # todo Замените на нужный email получателя
                fail_silently=False,
            )
            messages.success(request, 'Сообщение успешно отправлено!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
