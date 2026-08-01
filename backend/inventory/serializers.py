from rest_framework import serializers
from .models import Category, Product, Stock


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'chain', 'name']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'chain', 'category', 'name', 'barcode', 'price', 'created_at']


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'branch', 'product', 'quantity', 'low_stock_threshold', 'updated_at']