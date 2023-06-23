from django.db import models

# Create your models here.
menu=[
    {"id":1,"dish":"CB","price":120,"category":"non-veg"},
    {"id":2,"dish":"BB","price":130,"category":"non-veg"},
    {"id":3,"dish":"VB","price":110,"category":"non-veg"},
    {"id":4,"dish":"Sadhya","price":100,"category":"veg"},
    {"id":5,"dish":"Dosa","price":70,"category":"veg"},
]


#id=2
# res=[]

# for i in menu:
#     if i["id"]==id:
#         res.append(i)

# data=res.pop()

# data=[i for i in menu if i["id"]==id].pop()
# print(data)

class Menu(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    category=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    