from django.urls import path

from . import views



urlpatterns = [
    path('', views.index, name= 'index' ),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('<int:id>/', views.course, name="course"),
    path('courses', views.courses, name='courses')
    #path('<int:pk>/',views.CoursesDetailView.as_view(),name='detail')
]
