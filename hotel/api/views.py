from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import menu
from .serilizers import MenuSerilizer
from .models import Menu

# Create your views here.
# class Dishes(APIView):
#     def get(self,request):
#         if "category" in request.query_params:
#             qp=request.query_params.get("category")
#             dishes=[i for i in menu if i["category"]==qp]
#             return Response(data=dishes)
#         if "lmt" in request.query_params:
#             qp=request.query_params.get("lmt")
#             dishes=menu[0:int(qp)]
#             return Response(data=dishes)
#         return Response(data=menu)
#     def post(self,request,*args,**kwargs):
#         data=request.data
#         menu.append(data)
#         return Response(data=data)
    
# class SDish(APIView):
#     def get(self,request,*args,**kwargs):
#         id=kwargs.get("id")
#         data=[i for i in menu if i["id"]==id].pop()
#         return Response(data=data)
#     def delete(self,request,*args,**kwargs):
#         id=kwargs.get("id")
#         data=[i for i in menu if i["id"]==id].pop()
#         menu.remove(data)
#         return Response(data=data)
#     def put(self,request,*args,**kwargs):
#         id=kwargs.get("id")
#         data=request.data  
#         dish=[i for i in menu if i["id"]==id].pop()
#         dish.update(data)
#         return Response(data=dish)
    
class MenuView(APIView):
    def post(self,request):
        ser=MenuSerilizer(data=request.data)
        if ser.is_valid():
            name=ser.validated_data.get("name")
            pr=ser.validated_data.get("price")
            cat=ser.validated_data.get("category")
            Menu.objects.create(name=name,price=pr,category=cat)
            return Response({"msg":"ok"})
        return Response({"msg":"failed"})
    def get(self,request):
        if "category" in request.query_params:
            qp=request.query_params.get('category')
            dish=Menu.objects.filter(category=qp)
            ser=MenuSerilizer(dish,many=True)
            return Response(data=ser.data)
        dish=Menu.objects.all()
        ser=MenuSerilizer(dish,many=True)
        return Response(data=ser.data)
    
class SpecificItem(APIView):
    def get(self,request,*args,**kwargs):
        mid=kwargs.get("id")
        dish=Menu.objects.get(id=mid)
        ser=MenuSerilizer(dish)
        return Response(data=ser.data)
    def delete(self,request,*args,**kwargs):
        mid=kwargs.get("id")
        Menu.objects.filter(id=mid).delete()
        return Response({"msg":"item Deleted"})
    def put(self,request,*args,**kwargs):
        mid=kwargs.get("id")
        dish=Menu.objects.get(id=mid)
        ser=MenuSerilizer(data=request.data)
        if ser.is_valid():
            name=ser.validated_data.get("name")
            pr=ser.validated_data.get("price")
            cat=ser.validated_data.get("category")
            dish.name=name
            dish.price=pr
            dish.category=cat
            dish.save()
            return Response({"msg":"ok"})
        return Response({"msg":"failed"})
