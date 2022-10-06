from rest_framework import serializers
from ..models import Accounts_Roles

class Account_Role_serializers(serializers.ModelSerializer):

    class Meta:
        model = Accounts_Roles
        fields = ['is_active']