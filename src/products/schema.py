import graphene
from graphene_django import DjangoObjectType
from .models import Product


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'currency', 'category',)


class Query(graphene.ObjectType):
    products = graphene.List(ProductType)
    product_search = graphene.List(ProductType, search=graphene.String())

    def resolve_products(self, info):
        return Product.objects.all()

    def resolve_product_search(self, info, search):
        return Product.objects.filter(title__icontains=search)


schema = graphene.Schema(query=Query)
