from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path(r'schools/<course_id>', views.get_course, name='get_course'),
    path(r'courses/', views.all_courses, name='courses'),
    path(r'reviews/', views.all_comments, name='reviews'),
    path(r'contacts/', views.contacts, name='contacts'),
    path(r'apply/', views.apply, name='apply'),
]
