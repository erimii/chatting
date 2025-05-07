
# Django WebSocket Chatting App

이 프로젝트는 Django Channels와 WebSocket을 기반으로 만든 실시간 채팅 앱입니다.

## 주요 기술 스택

- Python 3.x
- Django
- Django Channels
- Redis (Channel Layer)
- WebSocket
- HTML + JavaScript (Vanilla)


## 주요 기능
- 실시간 채팅 (WebSocket)


## 디렉토리 구조 (일부)

```
chatting/
├── chat/                # 채팅 앱
│   ├── consumers.py     # WebSocket 로직
│   ├── models.py        # Room, Message 모델
│   ├── templates/chat/
│   │   └── room.html     # 채팅방 화면
│   └── views.py         # 방 뷰
├── chatting/            # Django 프로젝트
│   ├── asgi.py
│   ├── settings.py
├── manage.py
```
