from django.urls import path

from course.apps import CourseConfig
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, UserCreateAPIView, UserListAPIView

app_name = CourseConfig.name


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path('users/create/', UserCreateAPIView.as_view(), name='create_user'),
    path('users/', UserListAPIView.as_view(), name='list_user'),

] + router.urls