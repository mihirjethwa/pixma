# Generated by Django 2.1.4 on 2019-03-31 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixma', '0003_course_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='nooflectures',
            field=models.CharField(blank=True, max_length=244),
        ),
        migrations.AddField(
            model_name='course',
            name='time',
            field=models.CharField(blank=True, max_length=244),
        ),
    ]
