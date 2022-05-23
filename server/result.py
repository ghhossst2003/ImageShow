# coding=utf-8
import json
from enum import Enum
from enum import unique


@unique
class Status(Enum):
    SUCCESS = 0
    FAILURE = 1


def reply(status, message='', data=''):
    return json.dumps({'status': status.value, 'message': message, 'data': data})
