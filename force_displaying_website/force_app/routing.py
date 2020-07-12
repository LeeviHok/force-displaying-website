from django.urls import path

from force_app import consumers


websocket_urlpatterns = [
    path('ws/force_api/', consumers.ForceApi),
    path('ws/force_chart/', consumers.ForceChart),
]
