import json

from channels.generic.websocket import WebsocketConsumer


class ForceDataApi(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        force = data['force']
        print(force)