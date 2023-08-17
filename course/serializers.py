from rest_framework import serializers
from course.models import Course, Lesson, Payment

MANYABLE = {'many': True, 'read_only': True}


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons_count(self, instance):
        return instance.lesson_set.all().count()


class PaymentSerializer(serializers.ModelSerializer):
    course = CourseSerializer(**MANYABLE)
    lesson = LessonSerializer(**MANYABLE)

    class Meta:
        model = Payment
        fields = '__all__'
