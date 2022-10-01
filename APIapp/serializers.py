from dataclasses import fields
from rest_framework import serializers as sz
from .models import *

class addProductserializer(sz.ModelSerializer):
    class Meta:
        model = addProduct
        fields = ['id','P_name','P_code','P_category','P_price','P_quantity']
    