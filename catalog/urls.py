from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page

from .views import (ProductDetailView, ProductListView, ProductCreateView,
                    ProductUpdateView, ProductDeleteView, ProductListCatalog)

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='products_detail'),
    path('create/', ProductCreateView.as_view(), name='products_create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='products_update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='products_confirm_delete'),
    path('category/<int:category_id>/', ProductListCatalog.as_view(), name='category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
