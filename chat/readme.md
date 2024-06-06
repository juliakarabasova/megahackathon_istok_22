# ChatMessage Model for Django Project

## Описание

`ChatMessage` - это модель для хранения сообщений в чате, содержащая информацию о сообщениях поддержки. Модель включает в себя информацию о пользователе, тексте сообщения и временной метке.

## Поля модели

- `user` (ForeignKey): Пользователь, отправивший сообщение (CustomUser).
- `message` (TextField): Текст сообщения.
- `timestamp` (DateTimeField): Временная метка сообщения (автоматически добавляется при создании).

## Использование

```python
from .models import ChatMessage
from users.models import CustomUser

# Пример создания нового сообщения
user = CustomUser.objects.get(pk=1)
message = ChatMessage(
    user=user,
    message="Привет, у меня возник вопрос по заказу.",
)
message.save()
```

Этот пример демонстрирует создание и сохранение нового сообщения в чате от конкретного пользователя.