from django.shortcuts import render
from rest_framework import viewsets, generics

from course.models import Course, Lesson, Payment
from course.serializers import CourseSerializer, LessonSerializer, PaymentSerializer


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


class PaymentCreateAPIView(generics.CreateAPIView):
    """Создание платежа"""
    serializer_class = PaymentSerializer
