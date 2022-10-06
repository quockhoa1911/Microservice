from django.db import models
import uuid
from django.utils import timezone
# Create your models here.
class ModelBase(models.Model):
    objects = models.manager
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    create_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)#call when model.save()
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ('create_at',)
