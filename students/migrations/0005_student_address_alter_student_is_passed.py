# Generated by Django 4.1.7 on 2023-03-15 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_student_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='is_passed',
            field=models.BooleanField(default=True),
        ),
    ]
