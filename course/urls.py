from django.urls import path

from course.apps import CourseConfig
from rest_framework.routers import DefaultRouter

from course.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView

app_name = CourseConfig.name


router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')


urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='create_lesson'),
    path('lesson/', LessonListAPIView.as_view(), name='list_lesson'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='get_lesson'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='update_lesson'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='delete_lesson'),

] + router.urls