from django.urls import path
from django.contrib.auth import views
# from .views import StudentListView, StudentDetailView, StudentCreateView
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('period/new/', PeriodCreateView.as_view(), name='period_new'),
    path('period/<int:pk>/', PeriodDetailView.as_view(), name='period_detail'),
    path('period/open/<int:period_id>/', view_period, name='view_period'),
    path('students/add/', StudentCreateView.as_view(), name='student_add'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_open'),
]