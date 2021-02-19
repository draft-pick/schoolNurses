from django.shortcuts import render, HttpResponse
from django.db.models import Count
from .models import *
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


def album_add(request):
    if request.method == "GET":
        form = PeriodsForm()
        return render(request, 'mainDir/periods/create.html', {'form': form})
    elif request.method == "POST":
        form = PeriodsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Saved.")
        return render(request, 'mainDir/periods/create.html', {'form': form})


class PeriodCreateView(CreateView):
    model = Periods
    template_name = 'mainDir/periods/create.html'
    fields = ['title', 'start_date', 'end_date', 'is_active']


