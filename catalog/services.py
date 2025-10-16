from catalog.models import Products


class ProductService:

    @staticmethod
    def prod_in_category(category_id):
        # Получаем все продукты в категории
        return Products.objects.filter(category_id=category_id)
