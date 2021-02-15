from django.shortcuts import render
from .models import *


def home(request):
    context = {
        'title': 'Главная страница',
    }
    return render(request, 'school/index.html', context=context)
