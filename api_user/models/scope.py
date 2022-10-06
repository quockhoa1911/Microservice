from django.db import models
from ..models import Roles

class Scopes(models.Model):
    role = models.ForeignKey(to=Roles,on_delete=models.CASCADE,related_name='scope',null=True,blank=True,default=None)
    scope_value = models.TextField(null=True,blank=True,default=None)

    class Meta:
        db_table = 'scopes'
