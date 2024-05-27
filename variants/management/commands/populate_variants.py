import random

from django.core.management.base import BaseCommand
from images.models import ItemImage  # Ensure correct import path
from items.models import InventoryItem  # Ensure correct import path
from variants.models import Variant  # Ensure correct import path


class Command(BaseCommand):
    help = 'Populates variants for selected inventory items'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to populate variants...'))
        self.populate_variants()

    def populate_variants(self):
        # Fetch all available images from the ItemImage model
        images = list(ItemImage.objects.all())

        # Make sure there are images in the database
        if not images:
            self.stdout.write(self.style.ERROR('No images found in the ItemImage model. Please make sure to populate images first.'))
            return

        # Randomly select 40 items from the inventory
        items = list(InventoryItem.objects.all())
        if len(items) < 40:
            self.stdout.write(self.style.ERROR('Not enough items in inventory to create variants.'))
            return
        selected_items = random.sample(items, 40)

        # Create variants for each selected item
        for item in selected_items:
            num_variants = random.randint(1, 3)  # Each item can have 1-3 variants
            for _ in range(num_variants):
                variant = Variant.objects.create(
                    item=item,
                    price=random.randint(item.price - 50, item.price + 50),  # Variant price close to item price
                    quantity=random.randint(1, item.quantity),  # Variant quantity not more than item quantity
                    description=f'Variant of {item.name}'
                )

                # Assign 1-3 random images per variant
                num_images = random.randint(1, 3)
                selected_images = random.sample(images, num_images)
                for image_instance in selected_images:
                    variant.images.add(image_instance)

        self.stdout.write(self.style.SUCCESS('Successfully populated variants for selected items.'))
