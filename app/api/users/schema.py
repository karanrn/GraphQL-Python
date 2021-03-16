import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene_sqlalchemy import SQLAlchemyConnectionField

from .models import User

class UserObject(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_users = SQLAlchemyConnectionField(UserObject)