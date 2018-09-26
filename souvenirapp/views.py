from django.shortcuts import get_object_or_404, render
from django.template.loader import get_template
from django.template import Context
from .models import City, Place, Person, Review

# Create your views here.
from django.http import HttpResponse

from django.contrib.auth.models import User

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def create(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'souvenirapp/create.html', {'user': user})
def review(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return HttpResponse("You are at the create review page %s" % user.username)

def search(request, user_id):
    query = request.POST.get('usr_query', False)
    print ("QUERY: ", query)
    t = get_template('souvenirapp/search_results.html')
    city = City.objects.get(name=query).id
    print("CITY ID", city)
    friendsList = Person.objects.get(user_id=user_id).get_friends()
    print("FRIENDS LIST", friendsList)
    reviews = []
    for friend in friendsList:
        rList = Review.objects.filter(user_id_id=friend)
        user = User.objects.get(id=friend)
        for rev in rList:
            place = Place.objects.get(id=rev.place_id_id)
            if place.city_id == city:
                reviews.append((rev,place,user))
    print("REVIEWS", reviews)
    return HttpResponse(t.render({'query':reviews}))
