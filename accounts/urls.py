from django.urls import path, include
from . import views
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

# Imported schema
from .schema import schema
app_name = "accounts_api"

urlpatterns = [
    path('user/', views.check_user.as_view(), name='get_user'),                         #Check user api
    path('auth/', include('dj_rest_auth.urls', namespace='djrest_api')),                #dj rest auth login, change password etc
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),    #GraphQL view


]