from django.urls import path

from force_app import consumers


websocket_urlpatterns = [
    path('ws/force_data_api/', consumers.ForceDataApi),
]
