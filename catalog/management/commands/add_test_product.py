from django.core.management.base import BaseCommand
from catalog.models import Category, Products
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):

        Category.objects.all().delete()
        Products.objects.all().delete()

        category, _ = Category.objects.get_or_create(name='Ягоды', description='.')

        products = [
            {'name': 'Брусника', 'category': category, 'price': 80, 'created_at': '2025-09-08',
             'updated_at': '2025-09-08'},
            {'name': 'Малина', 'category': category, 'price': 30, 'created_at': '2025-09-08',
             'updated_at': '2025-09-08'},
        ]

        for product in products:
            product, created = Products.objects.get_or_create(**product)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Book already exists: {product.name}'))

        call_command('loaddata', 'category_fixture.json')
        call_command('loaddata', 'products_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))
