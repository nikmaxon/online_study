from rest_framework import status
from rest_framework.test import APITestCase

from course.models import Course


# Create your tests here.
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


class LessonsTestCase(APITestCase):
    pass
