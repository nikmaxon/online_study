from rest_framework import serializers

from course.serializers import PaymentSerializer, MANYABLE
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    user_payment = PaymentSerializer(source='payment_set', **MANYABLE)

    class Meta:
        model = User
        fields = '__all__'
