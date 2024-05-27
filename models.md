### Описание моделей баз данных для каждой функциональной области

#### 1. Пользователи (Users)

**CustomUser**
- **ID**: Уникальный идентификатор пользователя.
- **Имя пользователя**: Логин пользователя (уникальный).
- **Пароль**: Хэшированный пароль.
- **Электронная почта**: Электронная почта пользователя (уникальная).
- **Имя**: Имя пользователя.
- **Фамилия**: Фамилия пользователя.
- **Дата регистрации**: Дата создания аккаунта.
- **Бонусные очки**: Количество бонусных очков пользователя.
- **Реферальный код**: Уникальный реферальный код для приглашений.

#### 2. Программа лояльности (Loyalty)

**LoyaltyTransaction**
- **ID**: Уникальный идентификатор транзакции.
- **Пользователь**: Ссылка на пользователя, связанного с транзакцией.
- **Количество очков**: Количество бонусных очков, участвующих в транзакции.
- **Тип транзакции**: Тип транзакции (начисление или списание).
- **Дата**: Дата и время выполнения транзакции.

#### 3. Заказы (Orders)

**Order**
- **ID**: Уникальный идентификатор заказа.
- **Пользователь**: Ссылка на пользователя, сделавшего заказ.
- **Продукт**: Ссылка на продукт, который был заказан.
- **Статус**: Текущий статус заказа (создан, обрабатывается, отправлен, доставлен, установлен).
- **Договор (PDF)**: Ссылка на PDF-файл договора.
- **Спецификация (PDF)**: Ссылка на PDF-файл спецификации.
- **3D Модель**: Ссылка на 3D модель продукта.
- **Дата заказа**: Дата создания заказа.
- **Дата завершения**: Дата завершения работ по заказу.
- **Дата доставки**: Дата доставки заказа.
- **Дата установки**: Дата установки заказа.

**OrderTimeline**
- **ID**: Уникальный идентификатор записи временной шкалы.
- **Заказ**: Ссылка на связанный заказ.
- **Дата**: Дата события.
- **Событие**: Описание события, произошедшего с заказом.

#### 4. Каталог мебели (Products)

**Product**
- **ID**: Уникальный идентификатор продукта.
- **Название**: Название продукта.
- **Описание**: Подробное описание продукта.
- **Цена**: Цена продукта.
- **Цветное изображение**: Ссылка на цветное изображение продукта.
- **Черно-белый эскиз**: Ссылка на черно-белый эскиз продукта.
- **3D Модель**: Ссылка на 3D модель продукта.
- **Категория**: Категория, к которой относится продукт.

#### 5. Запись на встречи (Appointments)

**Appointment**
- **ID**: Уникальный идентификатор записи на встречу.
- **Пользователь**: Ссылка на пользователя, записавшегося на встречу.
- **Дата и время**: Дата и время назначенной встречи.
- **Заметки**: Дополнительные заметки, связанные с встречей.

#### 6. Чат поддержки (Chat)

**ChatMessage**
- **ID**: Уникальный идентификатор сообщения.
- **Пользователь**: Ссылка на пользователя, отправившего сообщение.
- **Сообщение**: Текст сообщения.
- **Временная метка**: Дата и время отправки сообщения.

#### 7. Акции и новости (Promotions)

**Promotion**
- **ID**: Уникальный идентификатор акции.
- **Название**: Название акции.
- **Описание**: Подробное описание акции.
- **Дата начала**: Дата начала акции.
- **Дата окончания**: Дата окончания акции.
- **Активность**: Флаг активности акции.

**News**
- **ID**: Уникальный идентификатор новости.
- **Название**: Название новости.
- **Содержание**: Подробное содержание новости.
- **Дата публикации**: Дата и время публикации новости.

### Объяснение

Эти модели описывают основные сущности, которые будут использоваться в системе ISTOK для управления пользователями, программой лояльности, заказами, каталогом мебели, записями на встречи, поддержкой через чат, а также акциями и новостями. Каждая модель содержит атрибуты, необходимые для хранения и обработки соответствующих данных.

---

### Описание моделей баз данных для каждой функциональной области

#### 1. Пользователи (Users)

**models.py** (в приложении `users`):
```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Модель пользователя с дополнительными полями для бонусных очков и реферального кода.
    """
    loyalty_points = models.IntegerField(default=0)
    referral_code = models.CharField(max_length=100, unique=True, blank=True, null=True)
```
- **CustomUser**: Расширенная модель пользователя с дополнительными полями:
  - `loyalty_points`: Бонусные очки пользователя.
  - `referral_code`: Уникальный реферальный код.

#### 2. Программа лояльности (Loyalty)

**models.py** (в приложении `loyalty`):
```python
from django.db import models
from users.models import CustomUser

class LoyaltyTransaction(models.Model):
    """
    Модель транзакций программы лояльности, хранит данные о начислении и списании бонусов.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    points = models.IntegerField()
    transaction_type = models.CharField(max_length=10, choices=[('earn', 'Earn'), ('redeem', 'Redeem')])
    date = models.DateTimeField(auto_now_add=True)
```
- **LoyaltyTransaction**: Модель для хранения транзакций лояльности:
  - `user`: Связь с пользователем.
  - `points`: Количество бонусных очков.
  - `transaction_type`: Тип транзакции (начисление или списание).
  - `date`: Дата транзакции.

#### 3. Заказы (Orders)

**models.py** (в приложении `orders`):
```python
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
    contract_pdf = models.FileField(upload_to='contracts/')
    specification_pdf = models.FileField(upload_to='specifications/')
    model_3d = models.FileField(upload_to='3d_models/')
    order_date = models.DateField()
    completion_date = models.DateField()
    delivery_date = models.DateField()
    installation_date = models.DateField()

class OrderTimeline(models.Model):
    """
    Модель временной шкалы заказа, содержит ключевые события заказа.
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    date = models.DateField()
    event = models.CharField(max_length=100)
```
- **Order**: Модель для хранения данных о заказе:
  - `user`: Связь с пользователем.
  - `product`: Связь с продуктом.
  - `status`: Статус заказа.
  - `contract_pdf`: Договор в формате PDF.
  - `specification_pdf`: Спецификация в формате PDF.
  - `model_3d`: 3D модель заказа.
  - `order_date`: Дата заказа.
  - `completion_date`: Дата завершения работ.
  - `delivery_date`: Дата доставки.
  - `installation_date`: Дата монтажа.

- **OrderTimeline**: Модель для хранения временной шкалы заказа:
  - `order`: Связь с заказом.
  - `date`: Дата события.
  - `event`: Описание события.

#### 4. Каталог мебели (Products)

**models.py** (в приложении `products`):
```python
from django.db import models

class Product(models.Model):
    """
    Модель продукта, содержит информацию о мебели, включая изображения и 3D модель.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color_image = models.ImageField(upload_to='product_images/color/')
    bw_image = models.ImageField(upload_to='product_images/bw/')
    model_3d = models.FileField(upload_to='product_models/')
    category = models.CharField(max_length=50)
```
- **Product**: Модель для хранения данных о продукте:
  - `name`: Название продукта.
  - `description`: Описание продукта.
  - `price`: Цена продукта.
  - `color_image`: Цветное изображение продукта.
  - `bw_image`: Черно-белый эскиз продукта.
  - `model_3d`: 3D модель продукта.
  - `category`: Категория продукта.

#### 5. Запись на встречи (Appointments)

**models.py** (в приложении `appointments`):
```python
from django.db import models
from users.models import CustomUser

class Appointment(models.Model):
    """
    Модель встречи, содержит информацию о записи на встречу.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    notes = models.TextField(blank=True)
```
- **Appointment**: Модель для хранения данных о встрече:
  - `user`: Связь с пользователем.
  - `date_time`: Дата и время встречи.
  - `notes`: Заметки о встрече.

#### 6. Чат поддержки (Chat)

**models.py** (в приложении `chat`):
```python
from django.db import models
from users.models import CustomUser

class ChatMessage(models.Model):
    """
    Модель сообщения в чате, содержит информацию о сообщениях поддержки.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
```
- **ChatMessage**: Модель для хранения данных о сообщениях в чате:
  - `user`: Связь с пользователем.
  - `message`: Текст сообщения.
  - `timestamp`: Временная метка сообщения.

#### 7. Акции и новости (Promotions)

**models.py** (в приложении `promotions`):
```python
from django.db import models

class Promotion(models.Model):
    """
    Модель акции, содержит информацию о текущих акциях и скидках.
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)

class News(models.Model):
    """
    Модель новости, содержит информацию о новостях компании.
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
```
- **Promotion**: Модель для хранения данных об акциях:
  - `title`: Заголовок акции.
  - `description`: Описание акции.
  - `start_date`: Дата начала акции.
  - `end_date`: Дата окончания акции.
  - `active`: Флаг активности акции.

- **News**: Модель для хранения данных о новостях:
  - `title`: Заголовок новости.
  - `content`: Содержание новости.
  - `published_date`: Дата публикации новости.

### Следующие шаги

1. **Создание миграций**: 
   - Выполнение команд для создания и применения миграций.
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Настройка администратора**:
   - Создание суперпользователя.
   ```sh
   python manage.py createsuperuser
   ```

3. **Тестирование**: 
   - Написание тестов для всех моделей.
