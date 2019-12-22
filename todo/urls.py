from django.urls import path
from . import views

urlpatterns = [
    path('', views.todolist),
    path('create/', views.todoform, name='home'),
    path('list/', views.todolist, name='todoList'),
    path('<int:id>/edit/', views.todoedit, name='todoEdit'),
    path('<int:id>/delete/', views.todoDelete, name='todoDelete'),
]
