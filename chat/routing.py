#from django.conf.urls import url
from django.urls import re_path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    # custom chat url
    re_path(r'ws/chats/messages/(?P<my_id>\w+)/(?P<other_user_id>\w+)/(?P<chat_no>\w+)/$', ChatConsumer.as_asgi()),
]
