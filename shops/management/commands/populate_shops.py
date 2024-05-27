import random

from django.core.management.base import BaseCommand

from accounts.models import RiffraffUser
from api import admin
from shops.models import Shop  # Update 'myapp' to the actual app name where Shop is defined


from faker import Faker
fake = Faker()

class Command(BaseCommand):
    help = 'Automatically populates shops with random data for each admin and vendor'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to populate shops...'))
        self.populate_shops()

    def populate_shops(self):
        admins = RiffraffUser.objects.filter(user_type='admin')
        vendors = RiffraffUser.objects.filter(user_type='vendor')

        Faker.seed(0)

        # Create shops for vendors
        for vendor in vendors:
            if not Shop.objects.filter(vendor=vendor).exists():  # Ensure vendor doesn't already have a shop
                Shop.objects.create(
                    admin=random.choice(admins),
                    name=fake.company() ,
                    address=fake.address(),
                    city=fake.city(),
                    state=fake.state(),
                    country=fake.country(),
                    phone=fake.phone_number(),
                    vendor=vendor
                )

        self.stdout.write(self.style.SUCCESS('Successfully populated shops for all users.'))
