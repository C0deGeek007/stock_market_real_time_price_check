from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path('ws/asc/stockupdater/', consumers.StockConsumer.as_asgi()),
]
