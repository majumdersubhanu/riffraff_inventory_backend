from django.contrib import admin

from images.admin import InventoryItemImageInline
from images.models import ItemImage
from items.models import InventoryItem


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'shop']
    list_filter = ['shop',]
    fields = ['name', 'price', 'quantity', 'shop', 'description']
    inlines = [InventoryItemImageInline]
    raw_id_fields = ['shop']
    search_fields = ['name', 'shop__name']
    ordering = ['name']


admin.site.register(ItemImage)
