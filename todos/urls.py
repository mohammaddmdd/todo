from .views import Todolist, DetailTodo
from django.urls import path

urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view(), name='todo_detail'),
    path('', Todolist.as_view(), name='todo_list'),

]
