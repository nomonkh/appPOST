# Generated by Django 4.0.3 on 2022-04-16 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dxarid', '0006_remove_main_id_alter_main_lot_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='lot_id',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
