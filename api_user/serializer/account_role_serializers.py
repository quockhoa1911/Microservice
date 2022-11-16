from rest_framework import serializers
from ..models import Accounts_Roles
from ..serializer import Role_serializers

class Account_Role_serializers(serializers.ModelSerializer):
    role = Role_serializers(many=False,read_only=True)
    class Meta:
        model = Accounts_Roles
        fields = ['is_active','role']