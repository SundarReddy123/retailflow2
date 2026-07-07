from django.db import models
from shops.models import ShopChain, Branch
# Create your models here.
class Category(models.Model):
    chain=models.ForeignKey(ShopChain, on_delete=models.CASCADE, related_name='categories')
    name=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural="categories"

    def __str__(self):
            return self.name


class Product(models.Model):
    chain = models.ForeignKey(ShopChain, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    name = models.CharField(max_length=200)
    barcode = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.barcode})"
    

class Stock(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='stock_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='stock_items')
    quantity = models.PositiveIntegerField(default=0)
    low_stock_threshold = models.PositiveIntegerField(default=10)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('branch', 'product')
    
    