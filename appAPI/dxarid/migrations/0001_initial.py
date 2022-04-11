# Generated by Django 4.0.3 on 2022-04-10 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot_id', models.CharField(max_length=255)),
                ('lot_name', models.CharField(max_length=255)),
                ('lot_status', models.CharField(max_length=255)),
                ('lot_dateini', models.DateTimeField()),
                ('lot_date_end', models.DateTimeField()),
                ('lot_group', models.CharField(max_length=255)),
                ('seller_name', models.CharField(max_length=255)),
                ('seller_inn', models.CharField(max_length=255)),
                ('seller_region', models.CharField(max_length=255)),
                ('seller_rayon', models.CharField(max_length=255)),
                ('seller_address', models.CharField(max_length=255)),
                ('buyer_name', models.CharField(max_length=255)),
                ('buyer_inn', models.CharField(max_length=255)),
                ('buyer_account', models.CharField(max_length=255)),
                ('buyer_region', models.CharField(max_length=255)),
                ('buyer_rayon', models.CharField(max_length=255)),
                ('buyer_address', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'dxarid"."main',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot_id', models.CharField(max_length=255)),
                ('art_id', models.IntegerField()),
                ('p_product_name', models.CharField(max_length=255)),
                ('measure_gnk', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('one_price', models.IntegerField()),
                ('all_price', models.IntegerField()),
                ('descript', models.CharField(max_length=255)),
                ('tnvd_code', models.CharField(max_length=255)),
                ('expend_id', models.CharField(max_length=255)),
                ('plan_position_id', models.IntegerField()),
            ],
            options={
                'db_table': 'dxarid"."products',
                'managed': True,
            },
        ),
    ]
