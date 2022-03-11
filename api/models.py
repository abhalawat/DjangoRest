from django.db import models
from django.contrib.auth.models import User

class Species(models.Model):
   id = models.AutoField(
        primary_key=True
    )
   first = models.CharField(max_length=200)
   parent_n = models.ForeignKey('self', related_name='pagess', on_delete=models.CASCADE,null=True,blank=True)
   
   def __str__(self):
        return self.first


