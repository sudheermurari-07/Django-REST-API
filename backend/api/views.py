from django.shortcuts import render

from products.models import Product
from products.serializers import ProductSerializer

from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.http import JsonResponse

@api_view(["POST"])
def api_home(request, *args, **kwargs):

    # data = request.data
    # instance = Product.objects.all().order_by("?").first()
    # data={}
    # if instance:
    #     # data=model_to_dict(model_data, fields=['id','title','price'])
    #     data=ProductSerializer(instance).data
    # return Response(data)
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance=serializer.save()
        print(instance)
        # data=serializer.data
        return Response(serializer.data)
    

 
