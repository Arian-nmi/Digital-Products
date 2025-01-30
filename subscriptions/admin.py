from django.contrib import admin
from .models import Package, Subscription


class PackageAdmin(admin.ModelAdmin):
    list_display = ['title', 'sku', 'is_enable', 'price', 'duration']


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'package', 'created_at', 'expire_at']


admin.site.register(Package, PackageAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
