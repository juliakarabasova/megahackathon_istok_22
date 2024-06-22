from django.db import models
from users.models import CustomUser


class Appointment(models.Model):
    """
    Модель встречи, содержит информацию о записи на встречу.
    """
    CONTACT_METHOD_CHOICES = [
        ('phone', 'Телефон'),
        ('social', 'Соц сети'),
    ]

    PURPOSE_CHOICES = [
        ('kitchen', 'Кухня'),
        ('wardrobe', 'Шкаф'),
        ('hallway', 'Прихожая'),
        ('closet', 'Гардероб'),
        ('bathroom', 'Мебель для ванной'),
        ('kids', 'Мебель для детской'),
        ('living_room', 'Мебель для гостиной'),
        ('complex_order', 'Комплексный заказ'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    is_approved = models.BooleanField(default=False, verbose_name='Подтверждена')
    accepted_datetime = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True, verbose_name='Заметки')
    contact_method = models.CharField(max_length=10, choices=CONTACT_METHOD_CHOICES)  # Способ связи
    contact_info = models.CharField(max_length=255)  # Сам контакт
    requires_confirmation = models.BooleanField(default=False, verbose_name='Подтверждение')
    purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES, verbose_name='Цель')  # Цель: Какая мебель потребуется?
    requires_consultation = models.BooleanField(default=False, verbose_name='Консультация')

    def save(self, *args, **kwargs):
        if self.contact_method == 'phone':
            self.contact_info = self.user.phone_number if self.user.phone_number else self.contact_info
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user} {self.date_time}'



