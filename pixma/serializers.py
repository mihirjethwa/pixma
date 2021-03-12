from rest_framework import serializers
from .models import *

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
            model=Department
            fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
            model=Course
            fields = '__all__'

class TableContentSerializer(serializers.ModelSerializer):

    class Meta:
            model=TableContent
            fields = '__all__'
