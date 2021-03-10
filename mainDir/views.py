from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.db.models import Count
from tablib import Dataset
from datetime import datetime, date
from .models import *
from .forms import StudentsForm, StudentFormEdit
from django.views.generic.edit import CreateView
import openpyxl
from django.views.generic import ListView, DetailView, UpdateView
from openpyxl import Workbook, load_workbook
from docxtpl import DocxTemplate, Document
import datetime
from .resources import StudentsReource


def home(request):
    periods = Periods.objects.filter(is_active=1)
    # students_count = Periods.objects.annotate(number_of_period=Count('period'))
    context = {
        'periods': periods,
        'title': 'Главная страница',
        # 'students_count': students_count,
    }
    return render(request, 'mainDir/index.html', context=context)


def period_add(request):
    if request.method == "GET":
        form = PeriodsForm()
        return render(request, 'mainDir/periods/create.html', {'form': form})
    elif request.method == "POST":
        form = PeriodsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Saved.")
        return render(request, 'mainDir/periods/create.html', {'form': form,
                                                               'title': 'Добавить новый период',
                                                               })


class PeriodCreateView(CreateView):
    model = Periods
    template_name = 'mainDir/periods/create.html'
    fields = ['title', 'start_date', 'end_date', 'is_active']


class StudentCreateView(CreateView):
    model = Students
    template_name = 'mainDir/students/create.html'
    fields = ['keySchool', 'surname', 'name', 'patronymic', 'sex', 'birthday', 'snils', 'contract_date',
              'contract_number']


class StudentDetailView(DetailView):
    model = Students
    template_name = 'mainDir/students/detail.html'


# class StudentUpdateView(UpdateView):
#     model = Students
#     template_name = 'mainDir/students/edit.html'
#     fields = ['keySchool', 'surname', 'name', 'patronymic', 'sex', 'birthday', 'snils','contract_date',
#               'contract_number']


def new_student(request, school_id):
    period_item = Periods.objects.get(pk=school_id)
    initial_dict = {
        "keySchool": school_id,
    }
    form = StudentsForm(request.POST or None, initial=initial_dict)
    context = {
        'period_item': period_item,
        'form': form,
    }
    return render(request, 'mainDir/students/create.html', context)


def view_school(request, school_id):
    period_item = Periods.objects.get(pk=school_id)
    students_item = Students.objects.all().filter(keySchool=school_id)
    context = {
        'title': period_item.title,
        'period_item': period_item,
        'students_item': students_item,
    }
    return render(request, 'mainDir/periods/open.html', context=context)


def view_student(request, school_id, student_id):
    period_item = Periods.objects.get(pk=school_id)
    students_item = Students.objects.all().filter(keySchool=school_id)
    student_item = students_item.get(pk=student_id)
    context = {
        'title': student_item.surname,
        'period_item': period_item,
        'students_item': students_item,
        'student_item': student_item,
    }
    return render(request, 'mainDir/students/detail.html', context=context)


def edit_student(request, school_id, student_id):
    period_item = Periods.objects.get(pk=school_id)
    student_item = Students.objects.get(pk=student_id)
    form = StudentFormEdit(instance=student_item)
    if request.method == 'POST':
        form = StudentFormEdit(request.POST, instance=student_item)
        if form.is_valid():
            form.save()
            return redirect('view_student', school_id, student_id, )
    context = {'form': form, 'period_item': period_item, 'student_item': student_item, }
    return render(request, 'mainDir/students/edit.html', context=context)


def import_students(request, school_id):
    period_item = Periods.objects.get(pk=school_id)
    book = openpyxl.open("media/template_students.xlsx")

    sheet = book.active

    print(sheet[2][0].value)

    for row in range(2, sheet.max_row + 1):
        im_surname = sheet[row][0].value
        im_name = sheet[row][1].value
        im_patronymic = sheet[row][2].value
        im_birthday = sheet[row][3].value
    print(im_surname, im_name, im_patronymic, im_birthday)
    context = {
        'period_item': period_item,
    }

    return render(request, 'mainDir/students/import_students_list.html', context=context)


def upload_xlsx(request, school_id):
    if request.method == 'POST':
        person_resource = StudentsReource
        dataset = Dataset()
        new_person = request.FILES['myfile']
        school_num = school_id
        if not new_person.name.endswith('xlsx'):
            messages.info(request, 'wrong format')
            return render(request, 'mainDir/students/upload_xlsx.html')

        imported_data = dataset.load(new_person.read(), format='xlsx')
        for data in imported_data:
            value = Students(
                data[0],
                data[1] + school_num,
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
            )
            value.save()
    return render(request, 'mainDir/students/upload_xlsx.html')


def print_docx(request, school_id, student_id):
    period_item = Periods.objects.filter(pk=school_id)
    student_item = Students.objects.filter(pk=student_id)
    for student in student_item:
        for p in period_item:
            start_date = p.start_date.strftime('%d.%m')
            end_date = p.end_date.strftime('%d.%m.%Y')
            doc = DocxTemplate("media/temp_doc.docx")
            context = {
                'start_date': start_date,
                'end_date': end_date,
                'surname': student.surname,
                'name': student.name,
                'patronymic': student.patronymic,
            }
            doc.render(context)
            doc.save("media/generated_doc.docx")
            return render(request, 'mainDir/students/detail.html', context=context)


def whole_list_docx(request, school_id):
    period_item = Periods.objects.filter(pk=school_id)
    student_item = Students.objects.all().filter(keySchool=school_id)
    doc = DocxTemplate("media/whole_list.docx")
    for p in period_item:
        start_date = p.start_date.strftime('%d.%m')
        end_date = p.end_date.strftime('%d.%m.%y')

        context = {
            'student_item': student_item,
            'start_date': start_date,
            'end_date': end_date,
        }
        doc.render(context)
        doc.save("media/generated_whole_list.docx")
        return render(request, 'mainDir/students/whole_list.html', context=context)
