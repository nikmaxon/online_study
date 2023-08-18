from rest_framework import serializers

from course.serializers import PaymentSerializer, MANYABLE
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    user_payment_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def get_user_payment_count(self, instance):
        return instance.payment_set.all().count()
