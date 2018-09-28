from django.shortcuts import get_object_or_404, render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.template.loader import get_template
from django.template import Context
from .models import City, Place, Person, Review
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
def result(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'souvenirapp/results.html', {'user': user})

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

@api_view(['GET'])      
def search(request, city_name, user_id):
    city = City.objects.get(name=city_name).id
    friendsList = Person.objects.get(user_id=user_id).get_friends()

    reviews = []
    for friend in friendsList:
        rList = Review.objects.filter(user_id_id=friend)

        for rev in rList:
            place = Place.objects.get(id=rev.place_id_id)
            if place.city_id == city:
                reviews.append(rev)
    serializer = serializers.ReviewSerializer(reviews, many=True)
    return Response(serializer.data)
