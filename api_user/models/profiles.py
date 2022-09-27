from api_base.models import ModelBase
from django.db import models
from .payment_type import Payment_type
class Profiles(ModelBase):
    name = models.CharField(max_length=100,null=True,blank=True)
    gender = models.BooleanField(null=True)
    age = models.IntegerField(null=True,blank=True)
    email = models.CharField(max_length=100)
    certificate = models.CharField(max_length=99)
    payment_type = models.ManyToManyField(to=Payment_type,through='Profiles_Payment_type',related_name='profile',blank=True,null=True,default=None)
    class Meta:
        db_table = 'profiles'
