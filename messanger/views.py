from django.shortcuts import render
from django.http import HttpResponse





def Index(request):
    return render(request, 'chat.html')


def room(request, room_name):
    return render(request, "rooms.html", {"room_name": room_name})




# def chat_box(request, chat_box_name):
#
#     return render(request, "room.html", {"chat_box_name": chat_box_name})
#
#
