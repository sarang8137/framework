from django.db import models

# Create your models here.
menu=[
    {"id":1,"dish":"CB","price":120,"category":"non-veg"},
    {"id":2,"dish":"BB","price":130,"category":"non-veg"},
    {"id":3,"dish":"VB","price":110,"category":"non-veg"},
    {"id":4,"dish":"Sadhya","price":100,"category":"non-veg"},
    {"id":5,"dish":"Dosa","price":70,"category":"non-veg"},
]


id=2
# res=[]

# for i in menu:
#     if i["id"]==id:
#         res.append(i)

# data=res.pop()

data=[i for i in menu if i["id"]==id].pop()
print(data)