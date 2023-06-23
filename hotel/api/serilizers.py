from rest_framework import serializers

class MenuSerilizer(serializers.Serializer):
    name=serializers.CharField()
    price=serializers.IntegerField()
    category=serializers.CharField()