# from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from rest_framework.response import Response

class  Information_of_student(APIViews):
    def POST(self,request):
       first_name= request.data['first_name']
       a=student()
       a.first_name=first_name
       a.save()
