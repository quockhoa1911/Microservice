from django.db import models
from api_base.models import ModelBase
from ..models import Roles,Profiles
from django.contrib.auth.base_user import AbstractBaseUser

class Accounts(AbstractBaseUser,ModelBase):
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=690)
    roles = models.ManyToManyField(to=Roles,blank=True,null=True,related_name='account',default=None,through='Accounts_Roles')
    profile = models.ForeignKey(to=Profiles,on_delete=models.CASCADE,blank=True,null=True,related_name='account',default=None)

    USERNAME_FIELD = 'username'
    class Meta:
        db_table = 'accounts'
