from requests import post
from json import dumps
from logging import Handler, NOTSET

msg_types = ['text','markdown']


class SparkHandler(Handler):

    api = 'https://api.ciscospark.com/v1/'

    def __init__(self, key, room, msg_type='markdown', level=NOTSET):
        Handler.__init__(self, level=level)
        self.room = room
        assert msg_type in msg_types
        self.msg_attr = msg_type
        self.headers = {
            'Authorization': 'Bearer {}'.format(key),
            'Content-Type': 'application/json'
        }


    def emit(self, record):
        msg = self.format(record)
        params = {
            "roomId": "{}".format(self.room),
            self.msg_attr: "{}".format(msg)
        }
        endpoint = "/".join((self.api, 'messages'))
        r = post(endpoint, headers=headers, data=dumps(params))
        r.raise_for_status()


    def get_rooms(self):
        raise NotImplementedError
