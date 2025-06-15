from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings data'

    def handle(self, *args, **kwargs):
        sample_data = [
            {"title": "Cozy Cottage", "description": "A small cottage in the woods", "location": "Nairobi", "price_per_night": 50.0},
            {"title": "Beach House", "description": "Sunny and relaxing", "location": "Mombasa", "price_per_night": 120.0},
            {"title": "Mountain Cabin", "description": "Great for hiking trips", "location": "Mt. Kenya", "price_per_night": 75.0},
        ]

        for data in sample_data:
            Listing.objects.create(**data)

        self.stdout.write(self.style.SUCCESS("Successfully seeded listings data"))
