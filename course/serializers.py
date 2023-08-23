from rest_framework import serializers
from course.models import Course, Lesson, Payment
from course.validators import VideoURLValidator

MANYABLE = {'many': True, 'read_only': True}


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'

        validators = [
            VideoURLValidator(field_name='video_url'),
        ]


class CourseSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons(self, instance):
        return instance.lesson_set.all().count()


class PaymentSerializer(serializers.ModelSerializer):
    course = CourseSerializer(**MANYABLE)
    lesson = LessonSerializer(**MANYABLE)

    class Meta:
        model = Payment
        fields = '__all__'


class CourseCreateSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(**MANYABLE)

    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        lesson = validated_data.pop('lesson')
        course_item = Course.objects.create(**validated_data)

        for item in lesson:
            Lesson.objects.create(**item, course=course_item)

        return course_item
