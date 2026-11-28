from django.core.management import call_command
from django.core.management.base import BaseCommand
from catalog.models import Product, Category
import os
from config import settings


class Command(BaseCommand):
    help = 'Add products and categories to database'
    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        try:
            call_command('loaddata', os.path.join(settings.BASE_DIR, 'category_fixture.json'))
            call_command('loaddata', os.path.join(settings.BASE_DIR, 'product_fixture.json'))
        except:
            self.stdout.write(self.style.SUCCESS('Check the fixture files'))
        else:
            self.stdout.write(self.style.SUCCESS('Fixtures loaded successfully'))
