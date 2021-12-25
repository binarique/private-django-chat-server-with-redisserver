import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from .models import User, Chat, Message
from channels.consumer import SyncConsumer
from channels.db import database_sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['chat_no']
        self.my_id = self.scope['url_route']['kwargs']['my_id']
        self.other_user_id = self.scope['url_route']['kwargs']['other_user_id']
        self.room_group_name = 'chat_%s' % self.room_name
        self.mymessage = await database_sync_to_async(self.save_messages)()
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    def save_messages(self):
        messages = Message()
        return messages

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        self.mymessage.message = message
        self.mymessage.sender = self.my_id
        self.mymessage.reciever = self.other_user_id
        await database_sync_to_async(self.mymessage.save)()
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "name": text_data_json['name']
            }
        )

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message,
            "name": event['name']
        }))
