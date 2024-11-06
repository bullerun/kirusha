# Generated by Django 5.1.2 on 2024-11-05 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursovaya', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='twofactorauthentication',
            options={'ordering': ['-time_create', 'login'], 'verbose_name': 'Двухфакторная аутентификация', 'verbose_name_plural': 'Двухфакторная аутентификация'},
        ),
        migrations.AddField(
            model_name='twofactorauthentication',
            name='email',
            field=models.EmailField(default='default@example.com', max_length=254, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='twofactorauthentication',
            name='is_authentication',
            field=models.BooleanField(default=False, verbose_name='Авторизация'),
        ),
        migrations.AlterField(
            model_name='twofactorauthentication',
            name='login',
            field=models.CharField(max_length=255, verbose_name='Логин'),
        ),
        migrations.AlterField(
            model_name='twofactorauthentication',
            name='password',
            field=models.CharField(max_length=255, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='twofactorauthentication',
            name='photo',
            field=models.ImageField(upload_to='media/images', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='twofactorauthentication',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='twofactorauthentication',
            name='time_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Время изменения'),
        ),
    ]