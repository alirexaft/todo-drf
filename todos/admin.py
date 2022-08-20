from django.contrib import admin
from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'is_completed']
    list_editable = ['is_completed']
    list_display_links = ['title']
    search_fields = ['title']

