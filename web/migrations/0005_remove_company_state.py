# Generated by Django 4.2.7 on 2024-06-03 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_remove_student_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='state',
        ),
    ]
