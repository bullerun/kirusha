from django.db import models

# Create your models here.
class twoFactorAuthentication(models.Model):
    login = models.CharField(max_length=255, verbose_name = 'Логин')
    password = models.CharField(max_length=255, verbose_name = 'Пароль')
    photo = models.ImageField(upload_to="media/images", verbose_name = 'Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name = 'Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name = 'Время изменения')
    is_authentication = models.BooleanField(default=False, verbose_name = 'Авторизация')
    email = models.EmailField(default="test@test.test", verbose_name = 'Почта')

    def __str__(self):
        return self.login


    class Meta:
        verbose_name = 'Двухфакторная аутентификация'
        verbose_name_plural = 'Двухфакторная аутентификация'
        ordering = ['-time_create', 'login']