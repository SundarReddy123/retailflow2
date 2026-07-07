from django.db.models.signals import post_save
from django.dispatch import receiver
from sales.models import Sale
from shops.models import UserBranchRole
from suppliers.models import PurchaseOrder
from .models import AuditLog


@receiver(post_save, sender=Sale)
def log_sale_created(sender, instance, created, **kwargs):
    if created:
        AuditLog.objects.create(
            user=instance.cashier,
            action='created_sale',
            description=f"{instance.cashier} processed a sale of ₹{instance.total_amount} at {instance.branch.name}",
            branch=instance.branch
        )


@receiver(post_save, sender=UserBranchRole)
def log_staff_added(sender, instance, created, **kwargs):
    if created:
        scope = instance.branch.name if instance.branch else instance.chain.name
        AuditLog.objects.create(
            user=instance.added_by,
            action='added_staff',
            description=f"{instance.added_by} added {instance.user} as {instance.role} at {scope}",
            branch=instance.branch
        )


@receiver(post_save, sender=PurchaseOrder)
def log_po_status_change(sender, instance, created, **kwargs):
    if not created:
        AuditLog.objects.create(
            user=instance.created_by,
            action='updated_po_status',
            description=f"PO#{instance.id} status changed to {instance.status}",
            branch=instance.branch
        )