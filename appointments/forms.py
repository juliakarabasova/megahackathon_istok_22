from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    date_time = forms.DateTimeField(
        widget=forms.TextInput(attrs={'type': 'datetime-local'}),
        label='Дата и время'
    )

    class Meta:
        model = Appointment
        fields = ['date_time', 'notes', 'contact_method', 'contact_info', 'purpose', 'requires_consultation']


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    email = forms.EmailField(label='Email')
    INTEREST_CHOICES = [
        ('Кухня', 'Кухня'),
        ('Гардероб', 'Гардероб'),
        ('Прихожая', 'Прихожая'),
        ('Гостиная', 'Гостиная'),
        ('Полная мебелировка', 'Полная мебелировка'),
    ]

    CONTACT_METHOD_CHOICES = [
        ('phone', 'Позвонить'),
        ('telegram', 'Написать в Telegram'),
        ('whatsapp', 'Написать в WhatsApp'),
    ]

    interest = forms.MultipleChoiceField(choices=INTEREST_CHOICES, widget=forms.CheckboxSelectMultiple)
    phone_number = forms.CharField(label='Номер телефона', max_length=20)
    contact_method = forms.ChoiceField(label='Как с Вами связаться?', choices=CONTACT_METHOD_CHOICES)
