from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'views_counter')
    list_filter = ('title',)
    search_fields = ('title',)
