from rest_framework import serializers
from .models import Product
from decimal import Decimal
from rest_framework.reverse import reverse

class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )


    class Meta:
        model = Product
        fields = ['url','id','title', 'content', 'price', 'discount']

    def get_discount(self, obj):
        print(obj.id)
        return obj.price * Decimal('0.70')
    # def get_url(self,obj):
    #     # return f"products/{obj.id}/"
    #     request=self.context.get('request')
    #     return reverse('product-detail',kwargs={"pk":obj.pk},request=request)
    
    