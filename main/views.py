from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from .models import *
import openpyxl


def main(request):
    # book = openpyxl.Workbook()
    # sheet = book.active
    # sheet['A2'] = 'hello from Django'
    # book.save("first.xlsx")
    # book.close()
    student = Students.objects.all()
    period = Period.objects.all()
    context = {
        'title': 'Главная страница',
        'student': student,
        'period': period,
        # 'book': book
    }
    return render(request, 'main/index.html', context=context)


class StudentListView(ListView):
    model = Students
    template_name = 'main/index.html'


class PeriodDetailView(DetailView):
    model = Period
    template_name = 'main/period/detail.html'


class StudentDetailView(DetailView):
    model = Students
    template_name = 'main/detail.html'


class StudentCreateView(CreateView):
    model = Students
    template_name = 'main/create.html'
    fields = ['surname', 'name', 'patronymic', 'birthday',]


class StudentUpdateView(UpdateView):
    model = Students
    template_name = 'main/edit.html'
    fields = ['surname', 'name', 'patronymic', 'birthday',]