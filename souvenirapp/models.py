from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField(User,
                                     related_name='friends_of',
                                     symmetrical=False)
    def get_friends(self):
        return [p.id for p in self.friends.all()]
    
    def __str__(self):
            return self.user.__dict__['username']
    
class State(models.Model):
    name = models.CharField(max_length=2)
    def __str__(self):
        return self.name

    
class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name

    
class Place(models.Model):
    category = models.CharField(max_length=5)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, help_text='brief review', null=True)
    def __str__(self):
        return self.name


    
class Review(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    place_id = models.ForeignKey(Place, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    def __str__(self):
        return self.text


