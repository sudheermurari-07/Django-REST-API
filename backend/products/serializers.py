from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializers import UserPublicSerializer
from .models import Product
from . import validators

class ProductSerializer(serializers.ModelSerializer):
    owner=UserPublicSerializer(source='user', read_only=True)
    my_discount= serializers.SerializerMethodField(read_only=True)
    # url= serializers.SerializerMethodField(read_only=True)
    # url = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field="pk")
    title = serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_product_title])
    body=serializers.CharField(source='content')
    class Meta:
        model = Product
        fields = [
            'owner',
            'title',
            'pk',
            'body',
            'price',
            'sale_price',
            'my_discount',
            'public',
            'path',
            'endpoint',
        ]
    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__exact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already exists")
    #     return value
    
    def get_url(self,obj):
        # return f"/api/products/{obj.pk}/"
        request =   self.context.get('request')
        if request is None:
            return None
        return reverse("product-detail", kwargs={"pk":obj.pk}, request=request)
    
    def get_my_discount(self, obj):
        try:
            return obj.get_discount()
        except:
            return None