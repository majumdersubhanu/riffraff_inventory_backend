# Generated by Django 5.0.6 on 2024-05-27 05:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('images', '0002_alter_itemimage_image_alter_itemimage_name'),
        ('items', '0006_delete_itemimage_alter_inventoryitem_images'),
        ('shops', '0003_shop_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompositeItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('images', models.ManyToManyField(to='images.itemimage')),
                ('items', models.ManyToManyField(to='items.inventoryitem')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.shop')),
            ],
        ),
    ]
