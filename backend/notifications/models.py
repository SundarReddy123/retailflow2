from django.db import models
from shops.models import Branch
from inventory.models import Product


class Notification(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='notifications')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.message} ({self.branch.name})"