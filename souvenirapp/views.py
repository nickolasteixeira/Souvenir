from django.shortcuts import get_object_or_404, render

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
