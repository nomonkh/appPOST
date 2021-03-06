# Generated by Django 4.0.3 on 2022-04-12 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dxarid', '0004_remove_main_user_remove_products_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='all_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='art_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='descript',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='expend_id',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='lot_id',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='measure_gnk',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='one_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='p_product_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='plan_position_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='tnvd_code',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
