from django.shortcuts import render
from django.views.generic import ListView, DetailView
from room.models import Room, Message
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class RoomListView(ListView, LoginRequiredMixin):

    ## Login Required Fields
    login_url = 'login/'
    redirect_field_name = '/'

    model = Room
    template_name = 'room/roomList.html'
    context_object_name = 'rooms'
    slug_url_kwarg = 'room_slug'

    def get_queryset(self):
        return Room.objects.all().order_by('createDate')

def RoomDetailView(request, room_slug):
    room = Room.objects.get(slug__exact = room_slug)
    messages = Message.objects.filter(room__exact = room)[0:25]
    return render(request, 'room/roomDetail.html', {'room': room, 'messages': messages})
