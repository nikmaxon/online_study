from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters
from course.models import Course, Lesson, Payment
from course.serializers import CourseSerializer, LessonSerializer, PaymentSerializer, CourseCreateSerializer


# Курсы
class CourseViewSet(viewsets.ModelViewSet):
    """Отображение курсов"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


# Уроки
class LessonCreateAPIView(generics.CreateAPIView):
    """Создание урока"""
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    """Вывод списка уроков"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'date')
    ordering_fields = ('date',)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Вызов конкретного урока"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    """Изменение урока"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    """Удаление урока"""
    queryset = Lesson.objects.all()


# Платежи
class PaymentListAPIView(generics.ListAPIView):
    """Вывод списка платежей"""
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'date')
    ordering_fields = ('date',)


class PaymentCreateAPIView(generics.CreateAPIView):
    """Создание платежа"""
    serializer_class = PaymentSerializer
