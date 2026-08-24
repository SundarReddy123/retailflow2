from rest_framework import serializers
from django.db import transaction
from .models import Sale, SaleItem


class SaleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleItem
        fields = ['id', 'product', 'quantity', 'unit_price', 'subtotal']
        read_only_fields = ['subtotal']


class SaleSerializer(serializers.ModelSerializer):
    items = SaleItemSerializer(many=True)

    class Meta:
        model = Sale
        fields = ['id', 'branch', 'cashier', 'total_amount', 'payment_method', 'created_at', 'items']
        read_only_fields = ['total_amount']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        with transaction.atomic():
            sale = Sale.objects.create(**validated_data)
            total = 0
            for item_data in items_data:
                item = SaleItem.objects.create(sale=sale, **item_data)
                total += item.quantity * item.unit_price
            sale.total_amount = total
            sale.save(update_fields=['total_amount'])
        return sale