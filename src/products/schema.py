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
        if not info.context.user.is_authenticated:
            return Product.objects.none()
        return Product.objects.all()

    def resolve_product_search(self, info, search):
        if not info.context.user.is_authenticated:
            return Product.objects.none()
        return Product.objects.filter(title__icontains=search)


class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
