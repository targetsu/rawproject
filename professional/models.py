# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

 class professionalInfo(models.Model):
     first_name=models.TextField(blank=True,null=True,max_lenght=12)
     mobile=models.TextField(blank=True,null=True,max_length=12)
     last_name=models.TextField(blank=True,null=True,max_length=25)
      email=models.TextField(blank=True,null=True,max_length=30)


