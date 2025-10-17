from catalog.models import Products
from django.core.cache import cache


class ProductService:

    @staticmethod
    def prod_in_category(category_id):
        """
        Возвращает все продукты в указанной категории.
        """
        # Генерируем уникальный ключ для кеша
        cache_key = f'products_category_{category_id}'
        # Пытаемся получить данные из кеша
        products = cache.get(cache_key)
        if not products:
            # Если данных нет в кеше, получаем их из базы данных
            products = list(Products.objects.filter(category_id=category_id))
            cache.set(cache_key, products, timeout=60*10)
        return products

