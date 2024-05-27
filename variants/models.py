from django.db import models

from images.models import ItemImage
from items.models import InventoryItem


# Create your models here.
class Variant(models.Model):
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    images = models.ManyToManyField(ItemImage)

    def __str__(self):
        return f'{self.item.name} - variant'
