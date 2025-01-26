from django.contrib import admin
from .models import Category, Product, File


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent', 'title', 'is_enabled', 'created_at']
    list_filter = ['parent', 'is_enabled']
    search_fields = ['title']


class FileInlineAdmin(admin.StackedInline):
    model = File
    fields = ['title', 'file_type', 'file', 'is_enabled']
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_enabled', 'created_at']
    list_filter = ['is_enabled']
    search_fields = ['title']
    filter_horizontal = ['categories']
    inlines = [FileInlineAdmin]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)