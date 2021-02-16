from django.shortcuts import render
from django.db.models import Count
from .models import *
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, UpdateView


def home(request):
    periods = Period.objects.filter(is_active=1)
    students_count = Period.objects.annotate(number_of_period=Count('period'))
    context = {
        'periods': periods,
        'title': 'Главная страница',
        'students_count': students_count,
    }
    return render(request, 'school/index.html', context=context)


class PeriodCreateView(CreateView):
    model = Period
    template_name = 'school/periods/create.html'
    fields = ['title', 'date', 'is_active']


class PeriodDetailView(DetailView):
    model = Period
    template_name = 'school/periods/detail.html'


def view_period(request, period_id):
    period_item = Period.objects.get(pk=period_id)
    students_item = Students.objects.all().filter(keyPeriod=period_id)
    context = {
        'title': period_item.title,
        'period_item': period_item,
        'students_item': students_item,
    }
    return render(request, 'school/periods/open.html', context=context)


class StudentCreateView(CreateView):
    model = Students
    template_name = 'school/students/create.html'
    fields = ['keyPeriod', 'surname', 'name', 'patronymic', 'sex', 'birthday', 'snils']


class StudentDetailView(DetailView):
    model = Students
    template_name = 'school/students/detail.html'
