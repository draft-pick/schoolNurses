from django.urls import path
from django.contrib.auth import views
from .views import StudentListView, StudentDetailView, StudentCreateView
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('period/<int:period_id>/', view_period, name='view_period'),
    path('period/print', my_print, name='my_print'),
    path('period/print_me/<int:period_id>/', print_me, name='print_me'),
    path('students/new/', StudentCreateView.as_view(), name='student_new'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('students/<int:pk>/edit/', StudentUpdateView.as_view(), name='student_edit'),
]