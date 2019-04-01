from django.db import models

# Create your models here.
class Department(models.Model):
    d_name = models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.d_name


class Course(models.Model):
    name = models.CharField(max_length=200,blank=False)
    description = models.TextField(blank=True)
    createdby = models.CharField(max_length=200,blank=False)
    ratings = models.DecimalField(max_digits=2, decimal_places=1)
    image = models.CharField(max_length=244,blank=False)
    time = models.CharField(max_length=244,blank=False)
    nooflectures = models.CharField(max_length=244,blank=False)
    is_bestseller = models.BooleanField(default=False)
    is_highestrated = models.BooleanField(default=False)
    department = models.ForeignKey('Department', on_delete = models.DO_NOTHING)
    def __str__(self):
        return self.name

class TableContent(models.Model):
    c = models.ForeignKey('Course', on_delete = models.CASCADE)
    title = models.CharField(max_length=200,blank=False)
    lecture = models.CharField(max_length=200,blank=False)
    lecturelink = models.TextField(blank=False)
    def __str__(self):
        return str(self.c)
