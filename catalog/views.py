from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Products, Category
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from catalog.services import ProductService


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductListView(ListView):
    model = Products
    template_name = 'catalog/products_list.html'


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Products


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Products
    form_class = ProductForm
    template_name = 'catalog/products_form.html'
    success_url = reverse_lazy('catalog:products_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Products
    form_class = ProductForm
    template_name = 'catalog/products_form.html'
    success_url = reverse_lazy('catalog:products_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('catalog.can_unpublish_products'):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Products
    permission_required = 'catalog.can_unpublish_products'
    template_name = 'catalog/products_confirm_delete.html'
    success_url = reverse_lazy('catalog:products_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('catalog.can_unpublish_products'):
            return ProductModeratorForm
        raise PermissionDenied


class ProductListCatalog(ListView):
    """ Класс представления продуктов по категориям """
    model = Category
    template_name = 'catalog/category.html'
    context_object_name = 'category'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return Products.objects.filter(category_id=category_id)

    def get_context_data(self, **kwargs):
        # Получаем стандартный контекст данных из родительского класса
        context = super().get_context_data(**kwargs)
        # Получаем ID категории из объекта
        category_id = self.kwargs.get('category_id')
        # Добавляем в контекст продукты в категории
        context['prod_in_category'] = ProductService.prod_in_category(category_id)
        return context
