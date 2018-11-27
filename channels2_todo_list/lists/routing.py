from django.urls import path

from .consumers import TODOListConsumer

websocket_urlpatterns = [
    path('ws/list/<uuid:list_pk>/', TODOListConsumer)
]