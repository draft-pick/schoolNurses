from django.urls import path
from django.contrib.auth import views
# from .views import StudentListView, StudentDetailView, StudentCreateView
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('school/new/', period_add, name='period_add'),
    path('school/<int:school_id>/students/add/', new_student, name='newStudent'),
    path('school/students/<int:pk>/', StudentDetailView.as_view(), name='open_student'),
    path('school/<int:school_id>/students/import/', import_students, name='importStudent'),
    path('school/<int:school_id>/students/import_xlsx/', upload_xlsx, name='uploadXlsx'),
    path('school/open/<int:school_id>/', view_school, name='view_school'),
    ]