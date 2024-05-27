from django.db import models

from accounts.models import RiffraffUser


# Create your models here.
class Shop(models.Model):
    admin = models.ForeignKey(RiffraffUser, on_delete=models.CASCADE, related_name='shop_admin', default=None,
                              null=True, blank=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    vendor = models.ForeignKey(RiffraffUser, on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return self.name
