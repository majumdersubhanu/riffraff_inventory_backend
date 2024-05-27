import os
import random

from django.core.files import File
from django.core.management.base import BaseCommand

from images.models import ItemImage  # Update 'images' to your actual app name where ItemImage is defined
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = 'Populates random images'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to populate Image...'))
        self.populate_Image()

    def populate_Image(self):
        images_path = "C:/Users/subhanu/Downloads/demo"  # Update this path to the correct directory containing images
        image_files = [f for f in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, f))]

        # Make sure there are images in the directory
        if not image_files:
            self.stdout.write(self.style.ERROR('No images found in the specified directory.'))
            return

        # Populate the ItemImage model with images
        for _ in range(100):  # Adjust the range if you want to populate with a different number of images
            image_file = random.choice(image_files)
            image_path = os.path.join(images_path, image_file)

            # Generate a fake name for the image
            name = " ".join(fake.words(nb=random.randint(2,5)))

            # Create a new ItemImage instance
            item_image = ItemImage(name=name)
            with open(image_path, 'rb') as f:
                item_image.image.save(image_file, File(f), save=True)

            self.stdout.write(self.style.SUCCESS(f'Successfully added image: {image_file} as {name}'))

        self.stdout.write(self.style.SUCCESS('Successfully populated with 100 images.'))