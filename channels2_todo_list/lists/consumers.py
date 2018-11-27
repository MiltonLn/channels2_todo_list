import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import TODOList, Task


class TODOListConsumer(WebsocketConsumer):
    def connect(self):
        list_pk = self.scope['url_route']['kwargs']['list_pk']
        self.list = TODOList.objects.get(id=list_pk)
        self.list_group_name = f'list_{list_pk}'

        async_to_sync(self.channel_layer.group_add)(
            self.list_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.list_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        msg_type = data.get('type', None)

        if msg_type == 'create_task':
            self.create_task(data)
        elif msg_type == 'update_task':
            self.update_task(data)
        else:
            raise Exception(f'Method {msg_type} not supported')

    def create_task(self, data):
        description = data['description']
        task = self.list.task_set.create(description=description)
        async_to_sync(self.channel_layer.group_send)(
            self.list_group_name,
            {
                'type': 'refresh_list',
                'id': str(task.id),
                'description': description
            }
        )

    def update_task(self, data):
        uuid = data['uuid']
        value = data['value']
        self.list.task_set.filter(id=uuid).update(completed=value)
        async_to_sync(self.channel_layer.group_send)(
            self.list_group_name,
            {
                'type': 'toggle_task',
                'id': uuid,
                'value': value
            }
        )

    def toggle_task(self, event):
        self.send(text_data=json.dumps({
            'type': 'toggle_task',
            'id': event['id'],
            'value': event['value']
        }))

    def refresh_list(self, event):
        self.send(text_data=json.dumps({
            'type': 'refresh_list',
            'id': event['id'],
            'description': event['description']
        }))