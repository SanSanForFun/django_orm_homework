from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import ProductDetailView, ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='products_detail'),
    path('create/', ProductCreateView.as_view(), name='products_create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='products_update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='products_confirm_delete')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
