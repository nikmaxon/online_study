# Generated by Django 4.2.4 on 2023-08-24 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_subscription_text_subscription_sub_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='sub_name',
            new_name='course_name',
        ),
    ]
