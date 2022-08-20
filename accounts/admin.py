from django.contrib import admin
from .models import User
from todos.models import Todo


class BookInline(admin.StackedInline):
    model = Todo


@admin.register(User)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'password', 'email']
    list_editable = ['password', 'email']
    search_fields = ['username']
    list_display_links = ['username']
    inlines = [BookInline]
