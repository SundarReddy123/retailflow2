from rest_framework import serializers
from .models import Supplier, PurchaseOrder, PurchaseOrderItem


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'chain', 'name', 'contact_person', 'phone', 'email', 'address', 'created_at']


class PurchaseOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderItem
        fields = ['id', 'purchase_order', 'product', 'quantity_ordered', 'quantity_received', 'unit_price']


class PurchaseOrderSerializer(serializers.ModelSerializer):
    items = PurchaseOrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = PurchaseOrder
        fields = ['id', 'branch', 'supplier', 'status', 'created_by', 'created_at', 'updated_at', 'items']