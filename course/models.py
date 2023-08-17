from django.db import models
from users.models import NULLABLE


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    preview = models.ImageField(**NULLABLE, upload_to='course/', verbose_name='Превью')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='Курс')

    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(**NULLABLE, upload_to='course/', verbose_name='Превью')
    video_url = models.SlugField(**NULLABLE, verbose_name='Ссылка на видео')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Payment(models.Model):
    CASH = 'CASH'
    BANK = 'BANK'

    PAYMENT_METHOD_CHOICES = [
        (CASH, 'Наличные'),
        (BANK, 'Перевод'),
    ]

    user = models.ForeignKey("users.User", on_delete=models.CASCADE, **NULLABLE, verbose_name='Пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='Курс')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name='Урок')

    amount = models.IntegerField(verbose_name='сумма оплаты')
    method = models.CharField(max_length=4, choices=PAYMENT_METHOD_CHOICES, **NULLABLE, verbose_name='способ оплаты')
    date = models.DateField(auto_now_add=True, verbose_name='Дата оплаты')

    def __str__(self):
        return f'{self.amount}({self.method}) - {self.date}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
        ordering = ('-course', '-lesson', '-date', '-method')
