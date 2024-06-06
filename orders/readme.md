# Order Model for Django Project

## Описание

`Order` - это модель для хранения информации о заказах, включая информацию о пользователе, продукте, статусе заказа, цене и других связанных документах и датах.

## Поля модели

- `user` (ForeignKey): Пользователь, сделавший заказ (CustomUser).
- `product` (ForeignKey): Продукт, добавленный в заказ (Product).
- `status` (CharField): Статус заказа.
- `price` (DecimalField): Цена заказа.
- `check_pdf` (FileField): PDF-файл чека заказа (загружается в папку 'check/').
- `address` (CharField): Адрес доставки заказа.
- `contract_pdf` (FileField): PDF-файл контракта (загружается в папку 'contracts/').
- `specification_pdf` (FileField): PDF-файл спецификации (загружается в папку 'specifications/').
- `model_3d` (FileField): Файл 3D-модели (загружается в папку '3d_models/').
- `order_date` (DateField): Дата заказа.
- `completion_date` (DateField): Дата завершения работ.
- `delivery_date` (DateField): Дата доставки.
- `installation_date` (DateField): Дата монтажа.

## Статусы заказа

- `created`: Создан
- `processing`: Обрабатывается
- `shipped`: Отправлен
- `delivered`: Доставлен
- `installed`: Установлен

## OrderTimeline Model

## Описание

`OrderTimeline` - это модель для хранения ключевых событий заказа, включая дату и описание события.

## Поля модели

- `order` (ForeignKey): Связанный заказ.
- `date` (DateField): Дата события.
- `event` (CharField): Описание события.

## Использование

```python
from .models import Order, OrderTimeline
from users.models import CustomUser
from products.models import Product

# Пример создания нового заказа
user = CustomUser.objects.get(pk=1)
product = Product.objects.get(pk=1)
order = Order(
    user=user,
    product=product,
    status="created",
    price=100.00,
    check_pdf="path/to/check.pdf",
    address="123 Main St, City, Country",
    contract_pdf="path/to/contract.pdf",
    specification_pdf="path/to/specification.pdf",
    model_3d="path/to/3d_model.stl",
    order_date="2024-06-06",
    completion_date="2024-06-10",
    delivery_date="2024-06-15",
    installation_date="2024-06-20"
)
order.save()

# Пример добавления события во временную шкалу заказа
order_timeline_event = OrderTimeline(
    order=order,
    date="2024-06-06",
    event="Заказ создан"
)
order_timeline_event.save()
```

Этот пример демонстрирует создание и сохранение нового заказа и добавление события во временную шкалу этого заказа.