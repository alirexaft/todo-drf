from django.urls import path
from .views import ListTodo, DetailTodo, TodoCreation, TodoUpdate, TodoDelete

urlpatterns = [
    path('', ListTodo.as_view()),
    path('<int:pk>/', DetailTodo.as_view()),
    path('create/', TodoCreation.as_view()),
    path('update/<int:pk>/', TodoUpdate.as_view()),
    path('delete/<int:pk>/', TodoDelete.as_view()),
]
