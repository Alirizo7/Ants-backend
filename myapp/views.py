from django.shortcuts import render
from .serializers import *

from rest_framework import generics
from .models import *
from .serializers import ProductSerializer
from .serializers import AboutSerialzer
from rest_framework.decorators import api_view  
from .serializers import PhoneNameSerializer







class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class AboutList(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerialzer

class PhoneNameCreateView(generics.CreateAPIView):
    queryset = PhoneName.objects.all()
    serializer_class = PhoneNameSerializer



    


