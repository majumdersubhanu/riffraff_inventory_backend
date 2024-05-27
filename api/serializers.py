from rest_framework import serializers

from accounts.models import RiffraffUser
from items.models import InventoryItem
from images.models import ItemImage
from shops.models import Shop
from variants.models import Variant


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiffraffUser
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = '__all__'


class InventoryItemSerializer(serializers.ModelSerializer):
    images = ItemImageSerializer(many=True, read_only=True)

    class Meta:
        model = InventoryItem
        fields = '__all__'


class VariantSerializer(serializers.ModelSerializer):
    images = ItemImageSerializer(many=True, read_only=True)

    class Meta:
        model = Variant
        fields = '__all__'
