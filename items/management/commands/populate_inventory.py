import os
import random

from django.core.management.base import BaseCommand

from items.models import InventoryItem, ItemImage  # Update 'items' to your actual app name where InventoryItem and ItemImage are defined
from shops.models import Shop

from faker import Faker
fake = Faker()


class Command(BaseCommand):
    help = 'Populates inventory with random items and images'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to populate inventory...'))
        self.populate_inventory()

    def populate_inventory(self):
        # Fetch all available images from the ItemImage model
        images = list(ItemImage.objects.all())

        # Make sure there are images in the database
        if not images:
            self.stdout.write(self.style.ERROR('No images found in the ItemImage model. Please make sure to populate images first.'))
            return

        # Fetch all shops
        shops = Shop.objects.all()
        if not shops:
            self.stdout.write(self.style.ERROR('No shops found. Please make sure to populate shops first.'))
            return

        # Create 50 items
        for i in range(50):
            shop = random.choice(shops)
            item = InventoryItem.objects.create(
                name=' '.join(fake.words(nb=random.randint(1, 4))),
                price=random.randint(100, 1000),
                quantity=random.randint(1, 150),
                shop=shop,
                description=fake.paragraph(nb_sentences=random.randint(1, 6)),
            )

            # Assign 1-3 random images per item
            num_images = random.randint(1, 3)
            selected_images = random.sample(images, num_images)
            for image_instance in selected_images:
                item.images.add(image_instance)

        self.stdout.write(self.style.SUCCESS('Successfully populated inventory with 50 items.'))
