# Generated by Django 2.1.4 on 2019-03-31 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixma', '0004_auto_20190331_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.CharField(max_length=244),
        ),
        migrations.AlterField(
            model_name='course',
            name='nooflectures',
            field=models.CharField(max_length=244),
        ),
        migrations.AlterField(
            model_name='course',
            name='time',
            field=models.CharField(max_length=244),
        ),
    ]
