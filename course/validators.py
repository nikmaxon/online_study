from collections import OrderedDict
from rest_framework import serializers
from rest_framework.serializers import ValidationError

PROPER_DOMAINS = ['youtube.com', ]


class VideoURLValidator:

    def __init__(self, field_name: str):
        self.field_name = field_name

    def __call__(self, fields: OrderedDict) -> None:

        url = dict(fields).get(self.field_name)

        if url is not None and 'youtube.com' not in url:
            raise ValidationError('Не правильный url')