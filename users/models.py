from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {'null': True, 'blank': True}


class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')

    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='Страна', **NULLABLE)

    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER)
    is_active = models.BooleanField(default=False, verbose_name='Активация')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Subscription(models.Model):
    class Meta:
        verbose_name = 'Подписка на курс'
        verbose_name_plural = 'Подписки на курс'

    course_name = models.CharField(
        max_length=300, verbose_name='название подписки', **NULLABLE,
    )
    course = models.ForeignKey(
        'course.Course', verbose_name='курс для подписки', on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    user = models.ForeignKey(
        'users.User', verbose_name='пользователь', on_delete=models.CASCADE,
        related_name='subscriptions',
    )

    is_subscribed = models.BooleanField(default=False, verbose_name='Подписка оформлена')

    def __str__(self):
        return f'{self.course} {self.user}'

    def save(self, *args, **kwargs):
        self.course_name = self.course.title

        return super(Subscription, self).save(*args, **kwargs)
