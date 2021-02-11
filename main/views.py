from django.shortcuts import render
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


def view_period(request, period_id):
    period_item = Period.objects.get(pk=period_id)
    students_item = Students.objects.all().filter(keyPeriod=period_id)

    book = openpyxl.Workbook()
    sheet = book.active
    sheet['A1'] = 'Фамилия'
    row = 2
    for student in students_item:
        sheet[row][3] = student.id
        row += 1
    book.save("first.xlsx")
    book.close()
    context = {
        'title': period_item.title,
        'period_item': period_item,
        'students_item': students_item,
        'book': book
    }
    return render(request, 'main/period/detail.html', context=context)


class StudentListView(ListView):
    model = Students
    template_name = 'main/index.html'


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