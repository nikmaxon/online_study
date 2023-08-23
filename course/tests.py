from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from course.models import Course, Lesson


class LessonCRUDTestCase(APITestCase):

    def setUp(self):
        self.course = Course.objects.create(
            title='course test',
            description='course test'
        )

        self.lesson = Lesson.objects.create(
            title='lesson test',
            description='lesson test',
            course=self.course
        )

    def test_lesson_list(self):
        """ Тест получения списка уроков"""

        response = self.client.get(
            reverse('course:list_lesson'),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.lesson.id,
                        "title": self.lesson.title,
                        "description": self.lesson.description,
                        "preview": self.lesson.preview,
                        "video_url": self.lesson.video_url,
                        "is_public": self.lesson.is_public,
                        "course": self.lesson.course_id,
                        "owner": self.lesson.owner_id
                    },
                ]
            }
        )

    def test_create_lesson(self):
        """ Тест создания уроков"""
        pass
        


class CourseTestCase(APITestCase):

    def setUp(self):
        pass

    def test_list_course(self):
        """ Тестирование списка курсов """

        Course.objects.create(
            title='list test',
            description='list test'
        )

        response = self.client.get(
            '/courses/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [{'id': 2, 'lessons': 0, 'title': 'list test', 'preview': None, 'description': 'list test',
              'is_public': False,
              'owner': None}]
        )

    def test_create_course(self):
        """ Тестирование создания курсов """

        data = {
            "title": "Test",
            "description": "Test"
        }

        response = self.client.post(
            '/courses/',
            data=data
        )

        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 1, 'lessons': 0, 'title': 'Test', 'preview': None, 'description': 'Test', 'is_public': False,
             'owner': None}

        )

        self.assertTrue(
            Course.objects.all().exists()
        )
