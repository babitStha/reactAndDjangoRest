from django.http import JsonResponse
from django.shortcuts import render
import pkg_resources
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .products import products

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    return Response('Hello')
@api_view(['GET'])
def getProducts(request):
    return Response(products)

@api_view(['GET'])
def getProduct(request, pk):
    product = None
    for p in products:
        if p['_id'] == pk:
            product = p
    return Response(product)