from rest_framework.routers import DefaultRouter
from  products.models import Product
from products.viewsets import ProductViewSet 

router=DefaultRouter()
router.register('prod',ProductViewSet,basename='products')
urlpatterns=router.urls


