from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views



urlpatterns = [
    path('', views.index, name= 'index' ),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('<int:id>/', views.course, name="course"),
    path('courses', views.courses, name='courses'),
    path('api/department', views.DepartmentList.as_view()),
    path('api/course', views.CourseList.as_view()),
    path('api/tablecontent', views.TableContentList.as_view())
    # path('<int:pk>/',views.CoursesDetailView.as_view(),name='detail')
]
