
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatting.settings')

# application = get_asgi_application()

django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from chat import routing as chat_routing


application = ProtocolTypeRouter({
    "http": django_asgi_app,  # 기존 HTTP 처리
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat_routing.websocket_urlpatterns  # WebSocket 처리
        )
    ),
})