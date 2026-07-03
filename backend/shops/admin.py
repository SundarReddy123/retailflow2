from django.contrib import admin
from .models import ShopChain, Branch, UserBranchRole

# Register your models here.
admin.site.register(ShopChain)
admin.site.register(Branch)
admin.site.register(UserBranchRole)