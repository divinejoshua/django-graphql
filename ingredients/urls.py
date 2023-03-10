
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView

# Imported schema
from .schema import schema

urlpatterns = [
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
]