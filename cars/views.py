from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CarSerializer
from .models import Car

@api_view(['GET','POST'])
def cars_list(request):

    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True) # because we are using an all query(which would have many cars), set many to True
        return Response(serializer.data, status=status.HTTP_200_OK) # returns the data from the serializer as a response


    elif request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED) # returns the saved data and gives a 201 HTTP status
        