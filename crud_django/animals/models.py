from django.db import models

# Create your models here.

class Animals(models.Model):
    
    name=models.CharField(max_length=200,blank=False,null=False)
    species=models.CharField(max_length=200,blank=False,null=False)
    color=models.CharField(max_length=200,blank=False,null=False)
    extintion_warming=models.BooleanField()
    def __str__(self) :
        return self.name
   

