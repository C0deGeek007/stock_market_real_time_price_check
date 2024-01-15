import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from stockPlatform.routing import websocket_urlpatterns
from channels.sessions import SessionMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stockmarket.settings')

application = ProtocolTypeRouter({
    "http":get_asgi_application(),
    "websocket": SessionMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    )
})
