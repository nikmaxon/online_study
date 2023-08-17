from rest_framework import serializers

from course.serializers import PaymentSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    user_payment = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'
