# Generated by Django 5.0.6 on 2024-05-26 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
        ('variants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='images',
            field=models.ManyToManyField(to='images.itemimage'),
        ),
    ]