from django.urls import path
from .views import ProductList,AboutList,PhoneNameCreateView

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('abouts/', AboutList.as_view(), name='about-list'),
    path('create/',PhoneNameCreateView.as_view(),name='create_phone_name'),
    


]