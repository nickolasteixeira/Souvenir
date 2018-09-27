from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/<int:user_id>', views.create, name="create_itinerary"),
    path('review/<int:user_id>', views.review, name="write_review"),
    path('api/state_list/', views.state_list, name='state_list'),
    path('api/city_list/', views.city_list, name='city_list'),
    path('api/<int:city_id>/places', views.places_list, name='places_list'),
    path('api/<int:city_id>/<int:user_id>/places', views.places_by_rec, name='places_by_rec'),
    path('search/<str:user_id>', views.search, name="search"),
]
