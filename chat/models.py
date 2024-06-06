from django.db import models
from users.models import CustomUser

class ChatMessage(models.Model):
    """
    Модель сообщения в чате, содержит информацию о сообщениях поддержки.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

