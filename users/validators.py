from collections import OrderedDict
from rest_framework import serializers


class AlreadySubscribedCheck:

    def __call__(self, fields: OrderedDict) -> None:
        """Проверка при создании подписки на уже существующую подписку.
        Args:
            fields (OrderedDict): Поля сериализатора.

        Raises:
            serializers.ValidationError: Если пользователь уже подписан.
        """
        course, user = fields.items()
        course = course[1]
        user = user[1]

        subs = user.subscriptions.all()

        if subs.filter(course=course).exists():
            raise serializers.ValidationError(f'Пользователь уже подписан на этот курс.')
