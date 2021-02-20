from django.contrib import admin

from .models import *


class StudentsInline(admin.TabularInline):
    br_name = 'keyBranches'
    model = Students
    list_display = ('surname', 'name', 'patronymic')


@admin.register(Periods)
class PeriodsAdmin(admin.ModelAdmin):
    inlines = [StudentsInline]

# @admin.register(Periods)
# class PeriodAdmin(admin.ModelAdmin):
#     list_display = ('title', 'is_active', 'start_date', 'end_date')
#     list_display_links = ('title', 'is_active', 'start_date', 'end_date')
#
