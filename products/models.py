from django.db import models

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
    HALLWAY = 'hallway'
    DRESSER = 'dresser'
    RACK = 'rack'
    CATEGORY_CHOICES = [
        (KITCHEN, 'Кухня'),
        (WARDROBE, 'Гардероб'),
        (HALLWAY, 'Прихожая'),
        (DRESSER, 'Комод'),
        (RACK, 'Стеллаж'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/image/')  # Изображение
    design = models.ImageField(upload_to='product_images/design/')  # чб эскиз
    model_3d = models.FileField(upload_to='product_models/')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default=KITCHEN)
    purpose = models.CharField(max_length=10, choices=PURPOSE_CHOICES, default=HOME)  # Назначение
    shape = models.CharField(max_length=100)  # Форма изделия
    facade_material = models.CharField(max_length=100)  # Материал фасадов
    countertop_material = models.CharField(max_length=100)  # Материал столешницы
