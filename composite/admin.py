from django.contrib import admin

from composite.models import CompositeItem
from images.admin import CompositeItemImageInline

class CompositeItemInline(admin.TabularInline):
    model = CompositeItem.items.through
    extra = 1
    verbose_name = "Item"
    verbose_name_plural = "Items"

@admin.register(CompositeItem)
class CompositeItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price','shop']
    list_filter = ['shop',]
    fields = ['name', 'price', 'shop']
    inlines = [CompositeItemInline, CompositeItemImageInline]
    raw_id_fields = ['shop']
    search_fields = ['name', 'shop__name']
    ordering = ['name']