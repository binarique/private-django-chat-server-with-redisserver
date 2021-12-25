#from django.conf.urls import url
from django.urls import re_path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chats/messages/(?P<my_id>\w+)/(?P<other_user_id>\w+)/(?P<chat_no>\w+)/$',
        ChatConsumer.as_asgi()),
    # url(r'ws/chats/messages/(?P<my_id>\w+)/(?P<other_user_id>\w+)/(?P<chat_no>\w+)/$',
    #     ChatSyncConsumer.as_asgi()),
]
