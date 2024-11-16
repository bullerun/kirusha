# accounts/models.py
from django.db import models
from django.contrib.auth.models import User
import uuid


class UserRegistration(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to="profile_images/", null=True, blank=True)
    password = models.CharField(max_length=128)
    verification_code = models.UUIDField(default=uuid.uuid4)  # генерируем уникальный код подтверждения
    is_verified = models.BooleanField(default=False)  # статус подтверждения email

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(upload_to="profile_images/", null=True, blank=True)  # поле для изображения

    def __str__(self):
        return f"Профиль пользователя {self.user.username}"
