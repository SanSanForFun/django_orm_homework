from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from catalog.views import base, product
from . import views

app_name = 'catalog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('base/', base, name='base'),
    path('product/<int:pk>/', product, name='product')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
