from rest_framework import serializers
from .models import Product, Category



class CategorySerializers(serializers.ModelSerializer):
    class Meta :
        model = Category
        fields = ['id','name']
        read_only_fields = ['id']

class ProductSerializers(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta :
        model = Product
        fields =['name' ,'description','price','stock' ,'created_at','category']
        read_only_fields =['id','created_at']

