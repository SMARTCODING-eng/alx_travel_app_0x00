from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth import get_user_model
from faker import Faker
import random

User = get_user_model()
fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        # Create or get a host user
        host, created = User.objects.get_or_create(username='host_user', defaults={'email': 'host@example.com'})
        if created:
            host.set_password('hostpass123')
            host.save()

        # Create 10 sample listings
        for _ in range(10):
            Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(nb_sentences=5),
                price =round(random.uniform(50, 500), 2),
                host=host,
                address=fake.address(),
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with sample listings.'))
 