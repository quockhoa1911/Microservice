from rest_framework import serializers
from ..models import Profiles
from ..serializer import Payment_type_serializers

class Profile_serializers(serializers.ModelSerializer):
    payment_type = Payment_type_serializers(many=True,read_only=True)
    class Meta:
        model = Profiles
        fields = ['id','name','gender','age','phone_number','email','certificate','avatar','payment_type','province',
                  'province_code','ward','ward_code','district','district_code','address']

class Profile_write_serializers(serializers.ModelSerializer):

    class Meta:
        model = Profiles
        fields = ['email','certificate']
