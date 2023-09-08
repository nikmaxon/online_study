from django.urls import path

from course.apps import CourseConfig
from rest_framework.routers import DefaultRouter

from course.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, PaymentCreateAPIView, PaymentListAPIView, PaymentRetrieveAPIView
from users.apps import UsersConfig

app_name = UsersConfig.name


router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')


urlpatterns = [
    # Уроки
    path('lesson/create/', LessonCreateAPIView.as_view(), name='create_lesson'),
    path('lesson/', LessonListAPIView.as_view(), name='list_lesson'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='get_lesson'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='update_lesson'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='delete_lesson'),

    # Платежи
    path('payment/', PaymentListAPIView.as_view(), name='list_payment'),
    path('payment/create/', PaymentCreateAPIView.as_view(), name='create_payment'),
    path('payment/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='get_payment'),

] + router.urls