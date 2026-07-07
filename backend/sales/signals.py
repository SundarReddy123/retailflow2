from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SaleItem
from inventory.models import Stock


@receiver(post_save, sender=SaleItem)
def update_stock_on_sale(sender, instance, created, **kwargs):
    if created:
        instance.subtotal = instance.quantity * instance.unit_price
        instance.save(update_fields=['subtotal'])

        stock, _ = Stock.objects.get_or_create(
            branch=instance.sale.branch,
            product=instance.product,
            defaults={'quantity': 0}
        )
        stock.quantity = max(0, stock.quantity - instance.quantity)
        stock.save(update_fields=['quantity'])