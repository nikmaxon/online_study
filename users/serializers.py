from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    user_payment = serializers.IntegerField(source='amount_set.all')

    class Meta:
        model = User
        fields = '__all__'
