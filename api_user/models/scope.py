from django.db import models
from ..models import Roles
from api_base.models import ModelBase

class Scopes(ModelBase):
    role = models.ForeignKey(to=Roles,on_delete=models.CASCADE,related_name='scope',null=True,blank=True,default=None)
    scope_value = models.TextField(null=True,blank=True,default=None)

    class Meta:
        db_table = 'scopes'
