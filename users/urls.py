from django.urls import path
from course.apps import CourseConfig
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.apps import UsersConfig
from users.views import UserViewSet, UserCreateAPIView, UserListAPIView, UserUpdateAPIView, UserDestroyAPIView, \
    SubscriptionCreateAPIView, SubscriptionDestroyAPIView

app_name = UsersConfig.name


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    # Пользователи
    path('', UserListAPIView.as_view(), name='list_user'),
    path('create/', UserCreateAPIView.as_view(), name='create_user'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='update_user'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='delete_user'),

    #Подписка
    path('subscription/create/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('subscription/delete/<int:pk>/', SubscriptionDestroyAPIView.as_view(), name='subscription_delete'),

    # Токен
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


] + router.urls