from django.shortcuts import render, redirect
from .models import Todo

def index(request):
    todo = Todo.objects.all()

    if request.method == 'POST':
        new_todo = Todo()
        new_todo.title = request.POST.get('title')
        new_todo.save()

        return redirect('/')


    return render(request, 'index.html', {'todos': todo})

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')