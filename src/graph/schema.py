import users.schema
import products.schema
import graphene


class Query(users.schema.Query, products.schema.Query, graphene.ObjectType):
    pass


class Mutation(users.schema.Mutation, products.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
