from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('room/<str:room_name>', show_room, name='show_room'),
    path('room/<str:room_name>/create_post', create_post, name='create')
]