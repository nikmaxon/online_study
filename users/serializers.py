from rest_framework import serializers
from course.serializers import PaymentSerializer, MANYABLE
from users.models import User, Subscription
from datetime import date
from users.validators import AlreadySubscribedCheck


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
        validators = [AlreadySubscribedCheck()]


class MyTokenObtainPairSerializer(serializers.ModelSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email

        user.last_login = date.today()
        user.save()

        return token


class UserSerializer(serializers.ModelSerializer):
    user_payment_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def get_user_payment_count(self, instance):
        return instance.payment_set.all().count()
