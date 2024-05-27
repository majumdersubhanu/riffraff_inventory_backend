# Generated by Django 5.0.6 on 2024-05-26 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
        ('items', '0005_remove_itemimage_inventory_item_inventoryitem_images'),
        ('variants', '0002_alter_variant_images'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ItemImage',
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='images',
            field=models.ManyToManyField(to='images.itemimage'),
        ),
    ]
