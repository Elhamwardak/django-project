# Generated by Django 4.1.7 on 2023-03-15 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_delete_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_passed',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]