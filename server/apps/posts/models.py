from django.db import models

# Create your models here.


class Tool(models.Model):
    
    name = models.CharField(max_length=32)
    kind = models.CharField(max_length=32)
    description = models.TextField()
    
class Idea(models.Model):
    Tool_list = [('django','Django'), ('react','React'),('java','Java'),('c++','C++'),('python','Python')]
    name = models.CharField(max_length=32)
    image = models.FileField(blank=True,upload_to='idea/%Y%m%d')
    description = models.TextField()
    interest = models.IntegerField()
    devtool = models.CharField(max_length=52,choices=Tool_list)

    

