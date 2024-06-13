# Generated by Django 5.0.6 on 2024-06-13 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('kitchen', 'Кухня'), ('wardrobe', 'Гардероб'), ('hallway', 'Прихожая'), ('dresser', 'Комод'), ('rack', 'Стеллаж'), ('children', 'Мебель в детскую')], default='kitchen', max_length=10, verbose_name='Категория'),
        ),
    ]
