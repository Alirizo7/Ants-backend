from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name','price','image','size','description')



class AboutSerialzer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('title','about','cost')

class PhoneNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneName
        fields = ['id', 'name', 'phone']


# class PhoneSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PhoneName
#         fields = ('id', 'name','phone')



# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('name','about')







