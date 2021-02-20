from django.urls import path
from django.contrib.auth import views
# from .views import StudentListView, StudentDetailView, StudentCreateView
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('school/new/', period_add, name='period_add'),
    path('school/test/', home_view, name='home_view'),
    path('school/<int:school_id>/students/add/', new_student, name='newStudent'),
    path('school/open/<int:school_id>/', view_school, name='view_school'),
    ]