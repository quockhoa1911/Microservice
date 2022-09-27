from api_base.models import ModelBase
from django.db import models

class Roles(ModelBase):
    name = models.CharField(max_length=50,null=True,blank=True,default=None)

    class Meta:
        db_table = 'roles'
