from django.shortcuts import render, HttpResponse
from django.db.models import Count
from .models import *
from .forms import StudentsForm, InputForm
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, UpdateView
from openpyxl import Workbook, load_workbook
from docxtpl import DocxTemplate


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


def new_student(request, school_id):
    period_item = Periods.objects.get(pk=school_id)
    context = {
        'period_item': period_item,
        'form': StudentsForm,
    }
    return render(request, 'mainDir/students/create.html', context)


# Create your views here.
def home_view(request):
    context = {'form': InputForm()}
    return render(request, "mainDir/students/test.html", context)


def view_school(request, school_id):
    period_item = Periods.objects.get(pk=school_id)
    students_item = Students.objects.all().filter(keySchool=school_id)
    context = {
        'title': period_item.title,
        'period_item': period_item,
        'students_item': students_item,
    }
    return render(request, 'mainDir/periods/open.html', context=context)
