from django.urls import path
from django.contrib.auth import views
# from .views import StudentListView, StudentDetailView, StudentCreateView
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('school/new/', period_add, name='period_add'),
    path('school/<int:school_id>/students/add/', new_student, name='newStudent'),
    # path('school/students/<int:pk>/', StudentDetailView.as_view(), name='open_student'),
    path('school/<int:school_id>/open/student/<int:student_id>/edit/', edit_student, name='edit_student'),
    path('period/student/<int:pk>/pr_docx/', print_docx, name='print_docx'),
    path('school/<int:school_id>/students/import/', import_students, name='importStudent'),
    path('school/<int:school_id>/students/import_xlsx/', upload_xlsx, name='uploadXlsx'),
    path('school/<int:school_id>/open/', view_school, name='view_school'),

    path('school/<int:school_id>/open/student/<int:student_id>', view_student, name="view_student")
    ]