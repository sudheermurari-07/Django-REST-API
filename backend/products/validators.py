from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Product


def validate_title(value):
    qs = Product.objects.filter(title__exact=value)
    if qs.exists():
        raise serializers.ValidationError(f"{value} is already exists")
    return value


def validate_title_no_hello(value):
    if "hello" in value.lower():
        raise serializers.ValidationError("Hello is not allowed")
    return value



unique_product_title = UniqueValidator(queryset=Product.objects.all(), lookup='iexact')