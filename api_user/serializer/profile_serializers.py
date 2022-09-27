from rest_framework import serializers
from ..models import Profiles
from ..serializer import Payment_type_serializers

class Profile_serializers(serializers.ModelSerializer):
    payment_type = Payment_type_serializers(many=True)
    class Meta:
        model = Profiles
        fields = ['id','name','gender','age','email','certificate','payment_type']

class Profile_write_serializers(serializers.ModelSerializer):

    class Meta:
        model = Profiles
        fields = ['name','gender','age','email','certificate']
