from django.contrib import admin

from .models import *


@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_display_links = ('title', 'is_active')


@admin.register(Students)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic')
    list_display_links = ('surname', 'name', 'patronymic')
    search_fields = ('surname', 'name')
