from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display  = ('title', 'priority', 'status', 'due_date', 'owner')
    list_filter   = ('priority', 'status')
    search_fields = ('title',)