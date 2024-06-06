from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Модель пользователя с дополнительными полями для бонусных очков и реферального кода.
    """
    loyalty_points = models.IntegerField(default=0)  # Бонусные очки пользователя.
    referral_code = models.CharField(max_length=100, unique=True, blank=True, null=True)  # Уникальный реферальный код
    phone_number = models.CharField(max_length=12)  # Телефон пользователя
    newsletter = models.BooleanField(default=True)  # Согласие на рассылку (да/нет)
    register_date = models.DateTimeField(auto_now_add=True)  # Дата создания аккаунта
    add_info = models.JSONField()  # Дополнительная информация в формате json (Планы на ремонт, личная инфа)


class Loyalty(models.Model):
    """
    Модель программы лояльности.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    points = models.IntegerField()  # Количество бонусных очков
    transaction_type = models.CharField(max_length=10, choices=[('earn', 'Earn'), ('redeem', 'Redeem')])  # Тип транзакции (начисление или списание).


class LoyaltyTransaction(models.Model):
    """
    Модель транзакций программы лояльности, хранит данные о начислении и списании бонусов.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    points = models.IntegerField()  # Количество бонусных очков
    transaction_type = models.CharField(max_length=10, choices=[('earn', 'Earn'), ('redeem', 'Redeem')])  # Тип транзакции (начисление или списание).
    date = models.DateTimeField(auto_now_add=True)  # Дата транзакции.


class Referal(models.Model):
    """
    Модель рефералов.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='referal_user')  # Пользователь компании, кто рекомендовал
    new_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='referal_new_user')  # Пользователь, который пришел по реферальному коду
    promo = models.TextField()  # Акция: Какую акцию (подарок) пользователь выбрал за использование программы
    confirmation = models.BooleanField(default=False)  # Да, если новый пользователь оформил заказ.


class Promotion(models.Model):
    """
    Модель акции, содержит информацию о текущих акциях и скидках.
    """
    PROGRAM_CHOICES = [
        ('general', 'Общая акция'),
        ('loyalty', 'По лояльности'),
        ('referral', 'Реферальная'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)
    program = models.CharField(max_length=20, choices=PROGRAM_CHOICES, default='general', verbose_name='Программа')


class News(models.Model):
    """
    Модель новости, содержит информацию о новостях компании.
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
