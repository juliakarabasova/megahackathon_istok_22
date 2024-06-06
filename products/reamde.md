# Product Model for Django Project

## Описание

`Product` - это модель для хранения информации о продуктах, включая название, описание, цену, изображения и 3D-модель. Модель также содержит дополнительную информацию о категории, назначении, форме изделия и материалах.

## Поля модели

- `name` (CharField): Название продукта.
- `description` (TextField): Описание продукта.
- `price` (DecimalField): Цена продукта.
- `image` (ImageField): Изображение продукта (загружается в папку 'product_images/image/').
- `design` (ImageField): Черно-белый эскиз продукта (загружается в папку 'product_images/design/').
- `model_3d` (FileField): 3D-модель продукта (загружается в папку 'product_models/').
- `category` (CharField): Категория продукта.
- `purpose` (CharField): Назначение продукта.
- `shape` (CharField): Форма изделия.
- `facade_material` (CharField): Материал фасадов.
- `countertop_material` (CharField): Материал столешницы.

## Возможные назначения продукта

- `Домой`
- `В офис`
- `Детская`

## Использование

```python
from .models import Product

# Пример создания нового продукта
product = Product(
    name="Стол",
    description="Прекрасный стол для вашего дома.",
    price=99.99,
    image="path/to/image.jpg",
    design="path/to/design.jpg",
    model_3d="path/to/model.stl",
    category="Мебель",
    purpose="home",
    shape="Прямоугольный",
    facade_material="Дерево",
    countertop_material="Стекло"
)
product.save()
```

Этот пример демонстрирует создание и сохранение нового продукта в базе данных.