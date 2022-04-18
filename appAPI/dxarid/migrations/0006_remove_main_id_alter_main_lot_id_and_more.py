# Generated by Django 4.0.3 on 2022-04-16 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dxarid', '0005_alter_products_all_price_alter_products_art_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main',
            name='id',
        ),
        migrations.AlterField(
            model_name='main',
            name='lot_id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='lot_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dxarid.main'),
        ),
    ]
