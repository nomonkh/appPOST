# Generated by Django 4.0.3 on 2022-04-11 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dxarid', '0003_main_user_products_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main',
            name='user',
        ),
        migrations.RemoveField(
            model_name='products',
            name='user',
        ),
    ]
