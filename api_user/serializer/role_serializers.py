from rest_framework import serializers
from ..serializer import Account_Role_serializers
from ..models import Roles

class Role_serializers(serializers.ModelSerializer):
    # status = Account_Role_serializers(many=True,read_only=True,source="account_role")
    #if name field the same related name then no source else required source
    status = serializers.SlugRelatedField(source="account_role",read_only=True,many=True,slug_field="is_active")
    # get one more fields use slug else get two or than  use Serializer model
    class Meta:
        model = Roles
        fields = ['id','name','status']
