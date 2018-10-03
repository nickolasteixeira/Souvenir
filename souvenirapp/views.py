from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes, permission_classes, authentication_classes
from django.template.loader import get_template
from django.template import Context
from .models import City, Place, Person, Review, Trip
from django.http import HttpResponse, JsonResponse

from django.forms.models import model_to_dict

from django.contrib.auth.models import User
from . import serializers
from . import models

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
#def create(request, user_id):
#    user = get_object_or_404(User, id=user_id)
#    return render(request, 'souvenirapp/create.html', {'user': user})
def review(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'souvenirapp/review.html', {'user': user})
#    return HttpResponse("You are at the create review page %s" % user.username)
@csrf_exempt
def result(request, user_id):
    query = request.POST.copy()
    current_user = User.objects.get(id=user_id)
    trip = Trip.objects.create(user=current_user)
    trip.save()
    trip.places = []
    results={"eat":[], "play":[], "stay":[]}
    for key, value in list(query.items()):
        rev = Review.objects.get(id=key[0])
        r = query.pop(key)
        user = User.objects.get(id=r[1])
        place = Place.objects.get(id=r[0])
        trip.places.append(place.id)
        city = City.objects.get(id=place.city_id)
        if place.category == "Eat":
            results["eat"].append([rev, place, user])
        elif place.category == "Play":
            results["play"].append([rev, place, user])
        elif place.category == "Stay":
            results["stay"].append([rev, place, user])
        #results.append([rev, place, user])
    trip.name = "{}'s trip to".format(current_user.username)
    trip.save()
    print("******************")
    print(trip.name)
    print(trip.places)
    user = get_object_or_404(User, id=user_id)
    return render(request, 'souvenirapp/results.html', {'user': user,
                                                        'result': results})
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
def search(request, city_name, user_id, format=None):
    serialized = []
    AVAILABLE_SERIALIZERS = {'Person': serializers.PersonSerializer, 'State': serializers.StateSerializer, 'Review': serializers.ReviewSerializer, 'Place':serializers.PlaceSerializer, 'User':serializers.UserSerializer}

    city = City.objects.get(name=city_name).id
    friendsList = Person.objects.get(user_id=user_id).get_friends()
    reviews = []
    for friend in friendsList:
        rList = Review.objects.filter(user_id_id=friend)
        user = User.objects.get(id=friend)
        user = AVAILABLE_SERIALIZERS[user.__class__.__name__](user, many=False).data
        for rev in rList:
            place = Place.objects.get(id=rev.place_id_id)
            if place.city_id == city:
                place = AVAILABLE_SERIALIZERS[place.__class__.__name__](place, many=False).data
                rev = AVAILABLE_SERIALIZERS[rev.__class__.__name__](rev, many=False).data
                reviews.append([rev,place,user])
    
    return Response(reviews)

def trips(request, user_id):
    trips = Trip.objects.filter(user=user_id)
    t = get_template('souvenirapp/view_trips.html')
    user = get_object_or_404(User, id=user_id)
    return HttpResponse(t.render({'query':
                                  [trip.name for trip in trips if trip.places],
                                  'user': user}))
