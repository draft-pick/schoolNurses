from django.urls import path
from django.contrib.auth import views
# from .views import StudentListView, StudentDetailView, StudentCreateView
from .views import *

urlpatterns = [
    path('', home, name='home'),
]