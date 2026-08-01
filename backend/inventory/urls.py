from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, StockViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)
router.register('stock', StockViewSet)

urlpatterns = router.urls