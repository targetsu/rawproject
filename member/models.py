
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class student(models.Model):
    first_name=models.TextField(blank=True,null=True,max_length=10)
    mobile=models.IntegerField(null=True,blank=True)