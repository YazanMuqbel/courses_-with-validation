from django.urls import path     
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_course', views.add_course, name='add_course'),
    path('courses/destroy/<int:id>', views.course_info, name='view_course'),
    path('course/destroy/confim/<int:id>', views.delete_course, name='delete_course')  
	   
]
