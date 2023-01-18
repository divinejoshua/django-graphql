import graphene
from graphene_django import DjangoObjectType

from .models import Account

# Define the graphql interface for the models
class AccountType(DjangoObjectType):
    class Meta:
        model = Account
        fields = "__all__"


# Create the query 
class Query(graphene.ObjectType):
    get_user = graphene.List(AccountType)

    def resolve_get_user(root, info):
        # context will reference to the Django request
        if not info.context.user.is_authenticated:
            data = {}
            data['error'] = "not authenticated"
            return data

        # Get the authenticated user 
        print(info.context.user)
        return Account.objects.filter(email=info.context.user)


schema = graphene.Schema(query=Query)