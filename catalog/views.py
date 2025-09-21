from django.urls import reverse

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
    fields = ('name', 'category', 'price', 'image', 'description')
    success_url = reverse_lazy('catalog:products_list')


class ProductUpdateView(UpdateView):
    model = Products
    fields = ('name', 'price', 'description')
    success_url = reverse_lazy('catalog:products_list')


class ProductDeleteView(DeleteView):
    model = Products
    success_url = reverse_lazy('catalog:products_list')
