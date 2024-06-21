from django.db import models
from django.urls import reverse


class Product(models.Model):
    """
    Модель продукта, содержит информацию о мебели, включая изображения и 3D модель.
    """
    HOME = 'home'
    OFFICE = 'office'
    KIDS = 'kids'
    PURPOSE_CHOICES = [
        (HOME, 'Домой'),
        (OFFICE, 'В офис'),
        (KIDS, 'Детская'),
    ]
    KITCHEN = 'kitchen'
    WARDROBE = 'wardrobe'
    BATHROOM = 'bathroom'
    DRESSER = 'dresser'
    RACK = 'rack'
    CHILDREN = 'children'
    CATEGORY_CHOICES = [
        (KITCHEN, 'Кухня'),
        (WARDROBE, 'Гардероб'),
        (BATHROOM, 'Ванная комната'),
        (DRESSER, 'Комод'),
        (RACK, 'Стеллаж'),
        (CHILDREN, 'Мебель в детскую'),
    ]

    name = models.CharField(max_length=100, verbose_name='Название продукта')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='product_images/image/', verbose_name='Изображение')
    design = models.ImageField(upload_to='product_images/design/', blank=True, verbose_name='ЧБ эскиз')
    model_3d = models.FileField(upload_to='product_models/', blank=True, verbose_name='3д модель')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default=KITCHEN, verbose_name='Категория')
    purpose = models.CharField(max_length=10, choices=PURPOSE_CHOICES, default=HOME, verbose_name='Назначение')
    shape = models.CharField(max_length=100, blank=True, verbose_name='Форма изделия')
    facade_material = models.CharField(max_length=100, blank=True, verbose_name='Материал фасадов')
    countertop_material = models.CharField(max_length=100, blank=True, verbose_name='Материал столешницы')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.pk})