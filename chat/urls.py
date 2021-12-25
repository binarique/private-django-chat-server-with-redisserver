from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('chats/<str:user_id>/', views.Chats, name="chats"),
    path('chats/messages/<str:my_id>/<str:other_user_id>/<str:chat_no>/',
         views.Messages, name="room"),
]
