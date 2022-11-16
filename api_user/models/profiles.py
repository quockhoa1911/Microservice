from api_base.models import ModelBase
from django.db import models
from .payment_type import Payment_type
class Profiles(ModelBase):
    name = models.CharField(max_length=100,null=True,blank=True)
    gender = models.BooleanField(null=True)
    age = models.IntegerField(null=True,blank=True)
    phone_number = models.CharField(max_length=99,null=True, blank=True, default=None)
    email = models.CharField(max_length=100)
    certificate = models.CharField(max_length=99)
    avatar = models.TextField(null=True,blank=True,default=None)
    payment_type = models.ManyToManyField(to=Payment_type,through='Profiles_Payment_type',related_name='profile',blank=True,null=True,default=None)
    province = models.CharField(max_length=99,null=True,blank=True,default=None)
    province_code = models.CharField(max_length=99,null=True,blank=True,default=None)
    ward = models.CharField(max_length=99,null=True,blank=True,default=None)
    ward_code = models.CharField(max_length=99,null=True,blank=True,default=None)
    district = models.CharField(max_length=99,null=True,blank=True,default=None)
    district_code = models.CharField(max_length=99,null=True,blank=True,default=None)
    address = models.TextField(null=True,blank=True,default=None)
    class Meta:
        db_table = 'profiles'
