# Generated by Django 5.0.6 on 2024-06-06 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('notes', models.TextField(blank=True, verbose_name='Заметки')),
                ('contact_method', models.CharField(choices=[('phone', 'Телефон'), ('social', 'Соц сети')], max_length=10)),
                ('contact_info', models.CharField(max_length=255)),
                ('requires_confirmation', models.BooleanField(default=False, verbose_name='Подтверждение')),
                ('purpose', models.CharField(choices=[('kitchen', 'Кухня'), ('wardrobe', 'Шкаф'), ('hallway', 'Прихожая'), ('closet', 'Гардероб'), ('bathroom', 'Мебель для ванной'), ('kids', 'Мебель для детской'), ('living_room', 'Мебель для гостиной'), ('complex_order', 'Комплексный заказ')], max_length=20, verbose_name='Цель')),
                ('requires_consultation', models.BooleanField(default=False, verbose_name='Консультация')),
            ],
        ),
    ]