from django.contrib import admin
from django.urls import path, include
from room import views

app_name = 'room'

urlpatterns = [
    path('', views.RoomListView.as_view(), name='list'),
    path('<slug:room_slug>/', views.RoomDetailView, name = 'room-detail'),
]