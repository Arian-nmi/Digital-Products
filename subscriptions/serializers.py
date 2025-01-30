from rest_framework import serializers
from .models import Package, Subscription


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['title', 'description', 'avatar', 'price', 'duration']


class SubscriptionSerializer(serializers.ModelSerializer):
    package = PackageSerializer()

    class Meta:
        model = Subscription
        fields = ['package', 'created_at', 'expire_at']