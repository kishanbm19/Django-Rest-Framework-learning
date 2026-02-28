from rest_framework import serializers
from .models import Product
from decimal import Decimal

class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id','title', 'content', 'price', 'discount']

    def get_discount(self, obj):
        print(obj.id)
        return obj.price * Decimal('0.70')