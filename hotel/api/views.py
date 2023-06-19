from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import menu

# Create your views here.
class Dishes(APIView):
    def get(self,request):
        return Response(data=menu)
    
class SDish(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        data=[i for i in menu if i["id"]==id].pop()
        return Response(data=data)