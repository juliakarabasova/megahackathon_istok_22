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
    manufacturing_time = models.IntegerField(verbose_name='Срок изготовления (в днях)', default=45)
    dimensions = models.CharField(max_length=200, verbose_name='Размеры (ШхВхГ)', blank=True)
    materials = models.TextField(verbose_name='Материалы', blank=True)
    equipment = models.TextField(verbose_name='Наполнение', blank=True)
    image_2 = models.ImageField(upload_to='product_images/image/', verbose_name='Изображение 2', blank=True)
    image_3 = models.ImageField(upload_to='product_images/image/', verbose_name='Изображение 3', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.pk})

    def get_materials_list(self):
        return self.materials.split('\n') if self.materials else []

    def get_equipment_list(self):
        return self.equipment.split('\n') if self.equipment else []

