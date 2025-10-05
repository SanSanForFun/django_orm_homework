from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import BlogDetailView, BlogListView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('update/<int:pk>', BlogUpdateView.as_view(), name='blog_update'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='blog_confirm_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
