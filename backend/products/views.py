from django.shortcuts import render
from rest_framework import  generics, mixins

from . models import Product
from .serializers import ProductSerializer
from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin

class ProductListCreateAPIView(UserQuerySetMixin, StaffEditorPermissionMixin,generics.ListCreateAPIView): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [authentication.SessionAuthentication, TokenAuthentication ]
    
    def perform_create(self, serializer):
        # print(serializer.validated_data)
        title= serializer.validated_data.get('title')
        content= serializer.validated_data.get('content') or None
        if content is None:
            content=title
        serializer.save(user=self.request.user, content=content)

    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request=self.request
    #     user=request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     # print(request.user)
    #     return qs.filter(user=request.user)


product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(UserQuerySetMixin,StaffEditorPermissionMixin,generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field='pk'

product_detail_view = ProductDetailAPIView.as_view()

class ProductUpdateAPIView(StaffEditorPermissionMixin,generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.DjangoModelPermissions]
    lookup_field='pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content=instance.title


product_update_view = ProductUpdateAPIView.as_view()

class ProductDestroyAPIView(StaffEditorPermissionMixin,generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field='pk'

    def perform_update(self, instance):
        super().perform_destroy(instance)

product_destroy_view = ProductDestroyAPIView.as_view()


class  ProductMixinView( UserQuerySetMixin,StaffEditorPermissionMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        print(args,kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)
    
    def perform_create(self, serializer):
        # print(serializer.validated_data)
        title= serializer.validated_data.get('title')
        content= serializer.validated_data.get('content') or None
        if content is None:
            content="this is a single view cool stuff"
        serializer.save(content=content)

product_mixin_view = ProductMixinView.as_view()


# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # lookup_field='pk'

# product_list_view = ProductListAPIView.as_view()

