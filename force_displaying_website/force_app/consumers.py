import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from channels.generic.websocket import WebsocketConsumer


class ForceApi(WebsocketConsumer):
    def connect(self):
        # Join to group
        self.group_name = 'force_api_group'
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        force = data['force']

        # Send force data to force_chart_group
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'force_chart_group',
            {
                'type': 'force_chart.send',
                'force': force,
            }
        )

class ForceChart(WebsocketConsumer):
    def connect(self):
        # Join to group
        self.group_name = 'force_chart_group'
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    def receive(self, text_data):
        pass

    # Send force data to client
    def force_chart_send(self, event):
        force = event['force']
        self.send(text_data=json.dumps({
            'force': force
        }))
