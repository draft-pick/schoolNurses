from django.contrib import admin

from .models import *


@admin.register(Periods)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'start_date', 'end_date')
    list_display_links = ('title', 'is_active', 'start_date', 'end_date')

