from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Products
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class ProductListView(ListView):
    model = Products


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Products


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Products
    form_class = ProductForm
    template_name = 'catalog/products_form.html'
    success_url = reverse_lazy('catalog:products_list')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Products
    form_class = ProductForm
    template_name = 'catalog/products_form.html'
    success_url = reverse_lazy('catalog:products_list')


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
