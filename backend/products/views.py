
from  rest_framework import generics
from  .serializer import ProductSerializer
from .models import Product
# Create your views here.
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    def perform_create(self,serializer):
        print(serializer.validated_data)
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content')
        if content is None:
            content=title
        serializer.save(content=content)

class ProductListAPIView(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer



