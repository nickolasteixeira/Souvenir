from rest_framework import serializers
from django.contrib.auth.models import User
 
from . import models
 
class StateSerializer(serializers.ModelSerializer):
 
    class Meta: 
       model = models.State
       fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.City
        fields = '__all__'

class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Place
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Person
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Review
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','id')
