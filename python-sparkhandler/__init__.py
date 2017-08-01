from requests import post
from json import dumps

class SparkHandler(object):

    api = 'https://api.ciscospark.com/v1/'

    def __init__(self, key, room, msg_attr='text'):
        self.key = key
        self.room = room


    def emit(self, record):
        msg = self.format(record)
        endpoint = "/".join((self.api, 'messages'))
        headers = {'Authorization': 'Bearer {0}'.format(self.key), 'Content-Type': 'application/json'}
        r = post(endpoint, headers=headers, data=dumps(data))
