from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=64) #문자열 컬럼
    user = models.CharField(max_length=32)
    content = models.TextField()
    region = models.CharField(max_length=16)
    price = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    