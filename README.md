#### Настроить .env
#### Выполнить в терминале:
- создать БД
- `python manage.py migrate`
- `python manage.py loaddata data.json`
или
- `python manage.py fill`
- `python manage.py csu`
##### Пароль суперюзера:
```Python
LOGIN = admin@SkyPro.com
PASS = qazwsx229
```
- Создать в админке или зарегистрировать юзеров и назначить им группы