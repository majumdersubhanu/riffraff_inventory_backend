from django.contrib import admin
from django.utils.safestring import mark_safe

from images.admin import VariantImageInline
from variants.models import Variant

@admin.register(Variant)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ['item', 'price', 'quantity', 'description']
    list_filter = ['item__shop']
    fields = ['item', 'price', 'quantity', 'description']
    inlines = [VariantImageInline]
    search_fields = ['item', ]
    ordering = ['item']
