from django.db.models.signals import post_save
from django.dispatch import receiver
from inventory.models import Stock
from .models import Notification


@receiver(post_save, sender=Stock)
def check_low_stock(sender, instance, **kwargs):
    if instance.quantity < instance.low_stock_threshold:
        already_exists = Notification.objects.filter(
            branch=instance.branch,
            product=instance.product,
            is_read=False
        ).exists()

        if not already_exists:
            Notification.objects.create(
                branch=instance.branch,
                product=instance.product,
                message=f"Low stock alert: {instance.product.name} at {instance.branch.name} has only {instance.quantity} left."
            )