from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
 
# Create your views here.
from django.http import HttpResponse

from django.contrib.auth.models import User
from . import serializers
from . import models

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def create(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'souvenirapp/create.html', {'user': user})
def review(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return HttpResponse("You are at the create review page %s" % user.username)

@api_view(['GET', 'POST'])
def state_list(request):
#list all states
    if request.method == 'GET':
        states = models.State.objects.all()
        serializer = serializers.StateSerializer(states, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.StateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def city_list(request):
    if request.method == 'GET':
        cities = models.City.objects.all()
        serializer = serializers.CitySerializer(cities, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def places_list(request, city_id):
    if request.method == 'GET':
        city = get_object_or_404(models.City, id=city_id)
        places = models.Place.objects.filter(city_id=city.id)
        serializer = serializers.PlaceSerializer(places, many=True)
        return Response(serializer.data)
