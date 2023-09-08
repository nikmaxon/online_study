from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from course.models import Course, Lesson, Payment
from users.models import User


class LessonCRUDTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='test@test.com',
        )
        self.user.set_password('test')
        self.user.save()

        self.course = Course.objects.create(
            title='course test',
            description='course test'
        )

        self.lesson = Lesson.objects.create(
            title='lesson test',
            description='lesson test',
            course=self.course,
            owner=self.user
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

        # print(response.json())

        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': self.lesson.pk, 'title': 'lesson test', 'description': 'lesson test', 'preview': None,
                 'video_url': None,
                 'is_public': False, 'course': self.course.pk, 'owner': self.user.pk}]}
        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_create_lesson(self):
        """ Тест создания уроков"""

        data = {
            'title': 'test create',
            'description': 'test create'
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            reverse('course:create_lesson'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_lesson_retrieve(self) -> None:
        """ Тест просмотра урока """
        self.client.force_authenticate(user=self.user)

        response = self.client.get(f'/lesson/{self.lesson.pk}/')

        self.assertEqual(
            response.status_code, status.HTTP_200_OK,
        )
        response = response.json()

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_lesson_update(self):
        """ Тест обновления урока """
        self.client.force_authenticate(user=self.user)

        data = {
            'title': 'update lesson',
            'description': 'update lesson',
        }

        response = self.client.put(
            path=f'/lesson/update/{self.lesson.pk}/',
            data=data,
        )

        self.assertEqual(
            response.status_code, status.HTTP_200_OK,
        )
        response = response.json()

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_lesson_delete(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.delete(
            f'/lesson/delete/{self.lesson.pk}/',
        )

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT,
        )
        self.assertFalse(
            Lesson.objects.all().exists(),
        )

    def tearDown(self) -> None:
        self.user.delete()
        self.course.delete()
        self.lesson.delete()


class ValodatorsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='test@test.com',
        )
        self.user.set_password('test')
        self.user.save()

        self.course = Course.objects.create(
            title='course test',
            description='course test'
        )

        self.lesson = Lesson.objects.create(
            title='lesson test',
            description='lesson test',
            course=self.course,
            owner=self.user
        )

    def test_lesson_validator_create(self):
        """ Тест создания   уроков"""

        data = {
            'title': 'test create validator',
            'description': 'test create validator',
            'video_url': 'sky@pro.ru'
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            reverse('course:create_lesson'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_course_validator_create(self):
        data = {
            "title": "Test",
            "description": "Test",
            "video_url": "sky@pro.ru"
        }

        response = self.client.post(
            '/courses/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )


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

        # print(response.json())

        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': 2, 'lessons': 0, 'title': 'list test', 'preview': None, 'description': 'list test',
                 'video_url': None, 'is_public': False, 'owner': None}]}
        )
        self.assertTrue(
            Course.objects.all().exists()
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

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        # print(response.json())

        self.assertEqual(
            response.json(),
            {'id': 1, 'lessons': 0, 'title': 'Test', 'preview': None, 'description': 'Test', 'video_url': None,
             'is_public': False, 'owner': None}
        )

        self.assertTrue(
            Course.objects.all().exists()
        )
