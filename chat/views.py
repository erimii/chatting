from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Room

def room(request, room_name):
    try:
        room_obj = Room.objects.get(name=room_name)
    except Room.DoesNotExist:
        return render(request, 'chat/room_not_found.html', {'room_name': room_name}, status=404)
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'room': room_obj,
        'user': request.user
    })

