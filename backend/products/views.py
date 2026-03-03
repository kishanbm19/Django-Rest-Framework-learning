
from  rest_framework import generics
from  .serializer import ProductSerializer
from .models import Product
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

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
@api_view(['GET','POST'])
def alt_view(request):
    if(request.method=='GET'):
        products=Product.objects.all()
        ser=ProductSerializer(products,many=True)
        return Response(ser.data)
    
    

    if(request.method=='POST'):
        serializer=ProductSerializer(data=request.data)
        if(serializer.is_valid(raise_exception=True)):
            serializer.save()
            return Response({"Product is added" },serializer.data)
        return Response(serializer.errors)

@api_view(['PUT'])
def updateapiview(request,pk):
    product=get_object_or_404(Product,pk=pk)
    serialize=ProductSerializer(product,data=request.data)
    print(get_object_or_404)

    serialize.is_valid(raise_exception=True)
    serialize.save()
    return Response({
          "message":f"product {pk} is updated","data":serialize.data})
@api_view(['DELETE'])
def deleteapiview(request,pk):
    product=get_object_or_404(Product,pk=pk)
    product.delete()
    
    return Response({
        "message":f"product with id {pk} is deleted"},
        status=status.HTTP_204_NO_CONTENT
       
    )
    




