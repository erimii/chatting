import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from .models import Message, Room
from django.contrib.auth.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # url 경로에서 방 이름 가져오기
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        # 그룹 이름 설정
        self.room_group_name = f'chat_{self.room_name}'

        # 현재 사용자 가져오기
        self.user = self.scope['user']

        # 그룹에 접속
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # 그룹에서 나가기
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        user = self.scope['user']

        # 메시지를 그룹으로 전송
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': user.username if user.is_authenticated else 'Anonymous',
                'timestamp': 'now'
            }
        )

    async def chat_message(self, event):
        message = event['message']
        user = event['user']
        timestamp = event['timestamp']

        # 그룹에서 받은 메시지를 클라이언트에 보내기
        await self.send(text_data=json.dumps({
            'type': 'chat_message',
            'message': message,
            'user': user,
            'timestamp': timestamp,
        }))