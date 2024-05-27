from django.db import models

class ItemImage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Item Image Name")
    image = models.ImageField(upload_to='images/', verbose_name="Item Image")

    def __str__(self):
        return self.name