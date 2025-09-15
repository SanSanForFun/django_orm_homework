from django.shortcuts import render

from catalog.models import Products


# Create your views here.

def home(request):
    return render(request, 'home.html')


def contacts(request):
    return render(request, 'contacts.html')


def base(request):
    goods = Products.objects.all()
    context = {'goods': goods}
    return render(request, 'goods.html', context)


def product(request, pk):
    prod = Products.objects.get(pk=pk)
    context = {'product': prod}
    return render(request, 'product.html', context)
