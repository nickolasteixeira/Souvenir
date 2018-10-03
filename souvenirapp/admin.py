from django.contrib import admin

# Register your models here.
from .models import Person, State, City, Place, Review, Trip

admin.site.register(Person)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Place)
admin.site.register(Review)
admin.site.register(Trip)
