from django.urls import path
from django.contrib.auth import views
# from .views import StudentListView, StudentDetailView, StudentCreateView
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('school/new/', period_add, name='period_add'),
    path('school/<int:school_id>/students/add/', new_student, name='newStudent'),
    # path('school/students/<int:pk>/', StudentDetailView.as_view(), name='open_student'),
    path('school/<int:school_id>/open/student/<int:student_id>/edit/', edit_student, name='edit_student'),

    path('school/<int:school_id>/open/student/<int:student_id>/spravka-dopusk/', print_docx, name='print_docx'),
    path('school/<int:school_id>/open/student/<int:student_id>/akt_job/', akt_job_docx, name='akt_job_docx'),
    path('school/<int:school_id>/open/student/<int:student_id>/certification/', certification_docx,
         name='certification_docx'),

    path('school/<int:school_id>/students/import/', import_students, name='importStudent'),
    path('school/<int:school_id>/students/import_xlsx/', upload_xlsx, name='uploadXlsx'),
    path('school/<int:school_id>/open/', view_school, name='view_school'),
    path('school/<int:school_id>/open/print', whole_list_docx, name='whole_list_docx'),

    path('school/<int:school_id>/open/student/<int:student_id>', view_student, name="view_student")
]
