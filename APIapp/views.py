from django.shortcuts import render
from .models import *
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
# Create your views here.

class addProductList(ListAPIView):
    def get(self,request,format=None):
        products = addProduct.objects.all()
        serializer = addProductserializer(products,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer =addProductserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    

class addProductDetail(APIView):
    def get_object(self,pk):
        try:
            return addProduct.objects.get(pk=pk)
        except addProduct.DoesNotExist:
            raise Http404    

    def get(self,request,pk,format=None):
        productadd = self.get_object(pk)
        serializer =addProductserializer(productadd)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        prductadd = self.get_object(pk)
        serializer = addProductserializer(prductadd,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    

    def delete(self,request,pk,format=None):
        productadd = self.get_object(pk)
        productadd.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class  registered_UserList(ListAPIView):
    def get(self,request,format=None):
        users = registerd_user.objects.all()
        serializer = registerd_userserializer(users,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer =registerd_userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

class  returnProductList(ListAPIView):
    def get(self,request,format=None):
        returns = addReturn.objects.all()
        serializer = addReturnserializer(returns,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer =addReturnserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

class saleProductList(ListAPIView):
    def get(self,request,format=None):
        sales = salesAdd.objects.all()
        serializer = saleSerializer(sales,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer =saleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)         