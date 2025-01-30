from django.contrib import admin
from .models import Gateway, Payment


class GatewayAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_enable']


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'package', 'gateway', 'price', 'status', 'phone_number', 'created_at']
    list_filter = ['status', 'gateway', 'package']
    search_fields = ['user__username', 'phone_number']


admin.site.register(Gateway, GatewayAdmin)
admin.site.register(Payment, PaymentAdmin)