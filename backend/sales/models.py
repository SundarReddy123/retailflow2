from django.db import models
from django.conf import settings
from shops.models import Branch
from inventory.models import Product
# Create your models here.
class Sale(models.Model):
    PAYMENT_CHOICES = [
        ('cash', 'Cash'),
        ('card', 'Card'),
        ('upi', 'UPI'),
    ]
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='sales')
    cashier = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='sales_made')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default='cash')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sale#{self.id} @ {self.branch.name} - ₹{self.total_amount}"

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sale_items')
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)

    def __str__(self):
        return f"{self.product.name} x{self.quantity} (Sale#{self.sale.id})"
