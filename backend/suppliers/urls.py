from rest_framework.routers import DefaultRouter
from .views import SupplierViewSet, PurchaseOrderViewSet, PurchaseOrderItemViewSet

router = DefaultRouter()
router.register('suppliers', SupplierViewSet)
router.register('purchase-orders', PurchaseOrderViewSet)
router.register('purchase-order-items', PurchaseOrderItemViewSet)

urlpatterns = router.urls