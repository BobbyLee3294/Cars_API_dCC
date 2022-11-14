from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer): # remember to add 'Serializer' in the class name
    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'year', 'price', 'dealership']
        depth = 1
        