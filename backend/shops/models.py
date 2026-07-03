from django.db import models
from django.conf import settings

# Create your models here.
class ShopChain(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='owned_chains'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Branch(models.Model):
    chain = models.ForeignKey(ShopChain, on_delete=models.CASCADE, related_name='branches')
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Branches"
    def __str__(self):
        return f"{self.name} ({self.chain.name})"
    


class UserBranchRole(models.Model):
    ROLE_CHOICES = [
        ('head_admin', 'Head Admin'),
        ('branch_admin', 'Branch Admin'),
        ('manager', 'Manager'),
        ('cashier', 'Cashier'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='branch_roles')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True, related_name='user_roles')
    chain = models.ForeignKey(ShopChain, on_delete=models.CASCADE, null=True, blank=True, related_name='user_roles')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='added_users',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        scope = self.branch.name if self.branch else self.chain.name
        return f"{self.user.username} - {self.role} @ {scope}"