from django.contrib import admin

from shops.models import Shop


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'city', 'state', 'country', 'phone', 'vendor']
    list_filter = ['city', 'state', 'country']
    fields = ['name', 'address', 'city', 'state', 'country', 'phone', 'vendor']
    search_fields = ['name', 'city', 'state', 'country']
    ordering = ['name']
