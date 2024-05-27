from django.db import models

from images.models import ItemImage
from items.models import InventoryItem
from shops.models import Shop

class CompositeItem(models.Model):
    name = models.CharField(max_length=100)
    items = models.ManyToManyField(InventoryItem)
    price = models.IntegerField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    images = models.ManyToManyField(ItemImage)
    
    def __str__(self) -> str:
        return self.name