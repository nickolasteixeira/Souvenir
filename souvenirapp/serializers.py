from rest_framework import serializers
 
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
