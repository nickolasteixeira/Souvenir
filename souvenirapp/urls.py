from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/<int:user_id>', views.create, name="create_itinerary"),
    path('review/<int:user_id>', views.review, name="write_review"),
    path('search/<str:user_id>', views.search, name="search"),
]
