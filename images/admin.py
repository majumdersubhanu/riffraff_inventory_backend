from django.contrib import admin

from composite.models import CompositeItem
from items.models import InventoryItem
from variants.models import Variant

# Register your models here.
class InventoryItemImageInline(admin.TabularInline):
    model = InventoryItem.images.through
    extra = 1
    verbose_name = "Item Image"
    verbose_name_plural = "Item Images"
    

class VariantImageInline(admin.TabularInline):
    model = Variant.images.through
    extra = 1
    verbose_name = "Item Image"
    verbose_name_plural = "Item Images"

class CompositeItemImageInline(admin.TabularInline):
    model = CompositeItem.images.through
    extra = 1
    verbose_name = "Item Image"
    verbose_name_plural = "Item Images"
    