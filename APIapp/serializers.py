from dataclasses import fields
from rest_framework import serializers as sz
from .models import *

class addProductserializer(sz.ModelSerializer):
    class Meta:
        model = addProduct
        fields = ['id','P_name','P_code','P_category','P_price','P_quantity']

class registerd_userserializer(sz.ModelSerializer):
    class Meta:
        model = registerd_user
        fields = ['id','first_name','last_name','email','mobile','user_type','username','password1']
        
class addReturnserializer(sz.ModelSerializer):
    class Meta:
        model = addReturn
        fields = ['id','P_name','P_code','P_category','P_quantity']

class saleSerializer(sz.ModelSerializer):
    class Meta:
        model = salesAdd
        fields = ['id','name','code','category','price','qnt']        
        