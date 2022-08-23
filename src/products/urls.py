from django.urls import path
from graph.schema import schema
from graph.views import PrivateGraphQLView


urlpatterns = [
    path("graphql/", PrivateGraphQLView.as_view(graphiql=True, schema=schema)),
]
