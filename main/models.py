from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    item = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    location = models.TextField()
    description = models.TextField()
    satisfaction = models.IntegerField()
   