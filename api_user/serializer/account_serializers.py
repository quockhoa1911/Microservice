from django.utils import timezone
from rest_framework import serializers
from ..models import Accounts
from ..serializer import Profile_serializers,Role_serializers,Profile_write_serializers

class Accounts_serializers(serializers.ModelSerializer):
    profile = Profile_serializers()
    role = Role_serializers()
    password = serializers.HiddenField(default=timezone.now)
    class Meta:
        model = Accounts
        fields = "__all__"

class Accounts_write_serializers(serializers.ModelSerializer):
    profile = Profile_write_serializers()
    class Meta:
        model = Accounts
        fields = ['username','password','role','profile']

    def create(self, validated_data):
        validated = validated_data.get('profile')
        if validated:
            profileserializers = Profile_write_serializers(data=validated)
            if profileserializers.is_valid(raise_exception=True):
                profile = profileserializers.save()
                validated_data['profile'] = profile
                accountinstance = super().create(validated_data)
                return accountinstance




