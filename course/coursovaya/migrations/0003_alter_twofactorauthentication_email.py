# Generated by Django 5.1.2 on 2024-11-05 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursovaya', '0002_alter_twofactorauthentication_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twofactorauthentication',
            name='email',
            field=models.EmailField(default='test@test.test', max_length=254, verbose_name='Почта'),
        ),
    ]
