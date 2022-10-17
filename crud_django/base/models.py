

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    #combination of null and black means is optional to fill and is possible to save as ""in the data base
    user= models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    title= models.CharField(max_length=200)
    description=models.TextField(max_length=300,null=True,blank=True)
    complete= models.BooleanField(default=False)
    created=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        #need to study this comand
        ordering=['complete']
         