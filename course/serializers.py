from rest_framework import serializers
from course.models import Course, Lesson, Payment

MANYABLE = {'many': True, 'read_only': True}


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(source='lesson_set.all', **MANYABLE)

    class Meta:
        model = Course
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
