import random

from django.core.management.base import BaseCommand

from accounts.models import RiffraffUser  # Update 'myapp' to the actual app name where your RiffraffUser is defined

from django.contrib.auth.models import Group

from faker import Faker
fake = Faker()


class Command(BaseCommand):
    help = 'Populates the database with random users'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to populate users...'))
        self.create_users()

    def create_users(self):
        # Create 3 Admins
        for _ in range(3):
            email = fake.ascii_free_email()
            curr_user = RiffraffUser.objects.create_user(email, user_type='admin', password='admin123')
            curr_user.first_name = fake.first_name()
            curr_user.last_name = fake.last_name()
            admin_grp = Group.objects.get(name = 'Admin')
            curr_user.groups.add(admin_grp)
            

        # Create Vendors and Buyers
        all_vendors = []
        for _ in range(6):  # You can change 6 to 8 if needed
            email = fake.ascii_free_email()
            vendor = RiffraffUser.objects.create_user(email, user_type='vendor', password='vendor123')
            vendor.first_name = fake.first_name()
            vendor.last_name = fake.last_name()
            vendor_grp = Group.objects.get(name = 'Vendor')
            curr_user.groups.add(vendor_grp)
            all_vendors.append(vendor)

        # Create 50 Buyers
        for _ in range(150):
            email = fake.ascii_free_email()
            curr_user = RiffraffUser.objects.create_user(email, user_type='buyer', password='buyer123')
            curr_user.first_name = fake.first_name()
            curr_user.last_name = fake.last_name()
            
            buyer_grp = Group.objects.get(name = 'Buyer')
            curr_user.groups.add(buyer_grp)


        self.stdout.write(self.style.SUCCESS(f'Created {len(all_vendors)} vendors and 150 buyers.'))
