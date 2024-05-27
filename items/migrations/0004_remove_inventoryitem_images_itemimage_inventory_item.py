# Generated by Django 5.1a1 on 2024-05-25 07:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('items', '0003_alter_inventoryitem_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventoryitem',
            name='images',
        ),
        migrations.AddField(
            model_name='itemimage',
            name='inventory_item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images',
                                    to='items.inventoryitem'),
            preserve_default=False,
        ),
    ]