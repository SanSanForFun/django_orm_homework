from django.urls import reverse
from catalog.forms import ProductForm
from catalog.models import Products
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.

class ProductListView(ListView):
    model = Products


class ProductDetailView(DetailView):
    model = Products


class ProductCreateView(CreateView):
    model = Products
    form_class = ProductForm
    template_name = 'catalog/products_form.html'
    success_url = reverse_lazy('catalog:products_list')


class ProductUpdateView(UpdateView):
    model = Products
    form_class = ProductForm
    template_name = 'catalog/products_form.html'
    success_url = reverse_lazy('catalog:products_list')


class ProductDeleteView(DeleteView):
    model = Products
    template_name = 'catalog/products_confirm_delete.html'
    success_url = reverse_lazy('catalog:products_list')
