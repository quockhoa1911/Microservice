from django.utils import timezone
from rest_framework import serializers
from ..models import Accounts,Profiles
from ..serializer import Profile_serializers,Account_Role_serializers,Role_serializers,Profile_write_serializers
from ..models import Accounts_Roles,Roles

class Accounts_serializers(serializers.ModelSerializer):
    profile = Profile_serializers()
    account_role = Account_Role_serializers(many=True,read_only=True)
    password = serializers.HiddenField(default=timezone.now)
    class Meta:
        model = Accounts
        fields = ['id','username','password','profile','account_role']

class Accounts_write_serializers(serializers.ModelSerializer):
    profile = Profile_write_serializers(write_only=True)
    class Meta:
        model = Accounts
        fields = ['username','password','roles','profile']
    def to_internal_value(self, data):
        #call before valid() field call, is hookpoint
        #use pre-proccesing data
        global Role_write
        global Profile_write
        Profile_write = data.get('profile')
        Role_write = data.get("roles")
        return super().to_internal_value(data) #missing value not in fields in database

    def create(self, validated_data):
        account_role = {}
        profile = Profiles.objects.create(**Profile_write)
        validated_data['profile'] = profile
        # save account
        accountinstance = super().create(validated_data)
        account_role["account"] = accountinstance
        account_role["role"] = Roles.objects.filter(id=Role_write).first()
        Accounts_Roles.objects.create(**account_role)
        #save role
        return accountinstance



