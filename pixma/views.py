from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.utils import timezone
from tablib import Dataset
from django.views.generic import View,TemplateView,ListView,DetailView
from .models  import *
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
# Create your views here.
def index(request):
    bcourses = Course.objects.filter(is_bestseller__exact=1)
    paginator = Paginator(bcourses, 6)
    page = request.GET.get('page')
    paged_bcourses = paginator.get_page(page)
    hcourses = Course.objects.filter(is_highestrated__exact=1)
    paginator = Paginator(hcourses, 6)
    page = request.GET.get('page')
    paged_hcourses = paginator.get_page(page)
    tablecontent = TableContent.objects.filter(c__exact= 2)
    context={
    'bcourses': paged_bcourses,
    'hcourses': paged_hcourses,
    'tablecontent': tablecontent
    }


    return render(request, 'pixma/index.html', context)

def course(request, id):
    course = get_object_or_404(Course, pk= id)
    tablecontent= TableContent.objects.filter(c__id= id)

    context = {
    'course': course,
    'tablecontent' : tablecontent
    }
    return render(request, 'pixma/course.html', context)
"""
class CoursesDetailView(DetailView):
        #model = Course
        #context_object_name = 'course'
        template_name = 'pixma/course.html'
        def get_queryset(self):
            return TableContent.objects.filter(c == id)
"""
def courses(request):
    courses=Course.objects.all()
    paginator = Paginator(courses, 12)
    page = request.GET.get('page')
    paged_courses = paginator.get_page(page)
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            courses = Course.objects.filter(name__icontains= keywords)
            paginator = Paginator(courses, 6)
            page = request.GET.get('page')
            paged_courses = paginator.get_page(page)
    context= {
    'courses': paged_courses
    }
    return render(request, 'pixma/courses.html', context)

def about(request):
    return render(request, 'pixma/about.html')

def contact(request):
    return render(request, 'pixma/contact.html')

class DepartmentList(APIView):
    def get(self, request):
        department1 = Department.objects.all()
        serializer = DepartmentSerializer(department1, many=True)
        return Response(serializer.data)

class CourseList(APIView):
    def get(self, request):
        course1 = Course.objects.all()
        serializer = CourseSerializer(course1, many=True)
        return Response(serializer.data)

class TableContentList(APIView):
    def get(self, request):
        table1 = TableContent.objects.all()
        serializer = TableContentSerializer(table1, many=True)
        return Response(serializer.data)
