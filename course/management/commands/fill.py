from django.core.management import BaseCommand

from course.models import Lesson, Payment


class Command(BaseCommand):

    def handle(self, *args, **options) -> None:

        Lesson.objects.all().delete()
        Payment.objects.all().delete()

        # Уроки
        lesson_list = [
            {'title': 'Django', 'description': 'Джан Го'},
            {'title': 'HTML', 'description': 'Эйч Ти Эм Эль'},
            {'title': 'CSS', 'description': 'Си Эс ЭС '},
            {'title': 'PHP', 'description': 'Пэ Ха Пэ'},
        ]

        lesson_for_create = []
        for lesson_item in lesson_list:
            lesson_for_create.append(
                Lesson(**lesson_item)
            )
        Lesson.objects.bulk_create(lesson_for_create)

        # Платежи
        payment_list = [
            {'amount': 300},
            {'amount': 250},
            {'amount': 350},
            {'amount': 400},
        ]

        payment_for_create = []
        for payment_item in payment_list:
            payment_for_create.append(
                Payment(**payment_item)
            )
        Payment.objects.bulk_create(payment_for_create)