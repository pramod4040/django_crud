from django.shortcuts import render, redirect, get_object_or_404
from todo.models import Tasks
from todo.forms import TodoForm
from django.contrib import messages
import pdb
# Create your views here.


def todoform(request):
    todoForm = TodoForm()
    if request.method == "POST":
        todoForm = TodoForm(request.POST)

        if todoForm.is_valid():
            # print(todoForm.cleaned_data)
            todoForm.save()
            messages.info(request, 'Todo Task Added Successfully.')
            # data = todoForm.cleaned_data
            # t1 = Tasks.objects.create(data)
            # t1.save()
            return redirect('/todo/list/')

    context = {
        'todoForm': todoForm
    }
    return render(request, "todo/home.html", context)


def todolist(request):
    taskList = Tasks.objects.all()
    context = {
        'taskList':taskList
    }
    return render(request, 'todo/list.html', context)

def todoedit(request, id):
    todo = get_object_or_404(Tasks, pk=id)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.info(request, 'Todo Edited Successfully.')
            return redirect('/todo/list/')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_edit.html', {'form':form})


def todoDelete(request, id):
    todo = get_object_or_404(Tasks, pk=id)
    todo.delete()
    messages.warning(request, 'Todo Deleted Successfully.')
    return redirect('/todo/list/')
