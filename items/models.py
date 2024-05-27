from django.db import models

from images.models import ItemImage
from shops.models import Shop



class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    description = models.TextField()
    images = models.ManyToManyField(ItemImage)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Inventory Item"
