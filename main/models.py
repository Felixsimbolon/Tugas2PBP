from django.db import models
import uuid
from django.contrib.auth.models import User


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    item = models.CharField(max_length=255)
    picture_link = models.TextField()
    time = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()
   