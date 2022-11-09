from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CarSerializer
from .models import Car

@api_view(['GET'])
def cars_list(request):
    cars = Car.objects.all()

    serializer = CarSerializer(cars, many=True) # because we are using an all query(which would have many cars), set many to True

    return Response(serializer.data) # returns the data from the serializer as a response