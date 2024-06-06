from django.db import models
from users.models import CustomUser
from products.models import Product

class Order(models.Model):
    """
    Модель заказа, содержит информацию о заказе, статусе и связанных документах.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[
        ('created', 'Created'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('installed', 'Installed')
    ])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    check_pdf = models.FileField(upload_to='check/')  # пдф чека заказа
    address = models.CharField(max_length=250)  # Адрес доставки заказа
    contract_pdf = models.FileField(upload_to='contracts/')
    specification_pdf = models.FileField(upload_to='specifications/')
    model_3d = models.FileField(upload_to='3d_models/')
    order_date = models.DateField()  # Дата заказа
    completion_date = models.DateField()  # Дата завершения работ
    delivery_date = models.DateField()  # Дата доставки
    installation_date = models.DateField()  # Дата монтажа


class OrderTimeline(models.Model):
    """
    Модель временной шкалы заказа, содержит ключевые события заказа.
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    date = models.DateField()  # Дата события
    event = models.CharField(max_length=100)  # Описание события
