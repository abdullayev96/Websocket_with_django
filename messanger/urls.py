from django.urls import path
from .views import *





urlpatterns = [
          path('', Index, name ="chat"),
          path("<str:room_name>/", room, name="room"),
          #path("<str:chat_box_name>/", chat_box, name="chat"),

]