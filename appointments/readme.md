# Appointment Model for Django Project

## Описание

`Appointment` - это модель для хранения информации о записях на встречу. Модель включает в себя информацию о пользователе, дате и времени встречи, способе связи, цели встречи и других дополнительных данных.

## Поля модели

- `user` (ForeignKey): Пользователь, связанный с записью (CustomUser).
- `date_time` (DateTimeField): Дата и время встречи.
- `notes` (TextField): Заметки к встрече (опционально).
- `contact_method` (CharField): Способ связи (телефон или соц сети).
- `contact_info` (CharField): Контактная информация.
- `requires_confirmation` (BooleanField): Требуется ли подтверждение встречи.
- `purpose` (CharField): Цель встречи (какая мебель потребуется).
- `requires_consultation` (BooleanField): Требуется ли консультация.

## Способы связи

- `phone`: Телефон
- `social`: Социальные сети

## Цели встречи

- `kitchen`: Кухня
- `wardrobe`: Шкаф
- `hallway`: Прихожая
- `closet`: Гардероб
- `bathroom`: Мебель для ванной
- `kids`: Мебель для детской
- `living_room`: Мебель для гостиной
- `complex_order`: Комплексный заказ

## Метод `save`

При сохранении объекта модели, если выбран способ связи `phone`, контактная информация автоматически заполняется номером телефона пользователя из его профиля, если он указан.

## Использование

```python
from .models import Appointment
from users.models import CustomUser

# Пример создания новой записи
user = CustomUser.objects.get(pk=1)
appointment = Appointment(
    user=user,
    date_time="2024-06-06 15:00",
    notes="Необходимо обсудить детали заказа",
    contact_method="phone",
    contact_info="",
    requires_confirmation=True,
    purpose="kitchen",
    requires_consultation=True
)
appointment.save()
```

Этот пример демонстрирует создание и сохранение новой записи на встречу для конкретного пользователя.