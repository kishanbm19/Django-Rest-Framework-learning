
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializer import ProductSerializer
import json
from products.models import Product
@api_view(["GET","POST","DELETE"])
def api_call(request):
    # model_data=Product.objects.all()
    # print(Product.objects.count())
    # data=[]
    # for p in model_data:
    #     data.append(model_to_dict(p))
    if request.method=='GET':
        products=Product.objects.all()
        serializer=ProductSerializer(products,many=True)
        print(products)
        return Response(serializer.data)
    
    if request.method=="POST":
        serializer=ProductSerializer(data=request.data)
        if(serializer.is_valid(raise_exception=True)):
            
            serializer.save()
            print(serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors)
    
    if(request.method=='DELETE'):
        id=request.data.get('id')
        try:

            p=Product.objects.get(id=id)
            p.delete()
            return Response("Deleted succesfully",status=200)
        except Product.DoesNotExist:
            return Response("Id not found")


    
       




















        # body = request.body
        # data = json.loads(body)

        # print("Data received:", data)

        # return JsonResponse({"message": "hi im kishan"})
# from django.http import JsonResponse

# def api_call(request):
#     query = request.GET.get("query")
#     print("Query received:", query)

#     return JsonResponse({"message": "hi im kishan"})
