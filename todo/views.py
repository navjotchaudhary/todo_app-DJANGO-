from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import TodoItem


def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html', {'all_todo_items': all_todo_items})


def addTodo(request):
    c = request.POST['content']
    if c:
        new_item = TodoItem(content=c)
        new_item.save()
        return HttpResponseRedirect('..')
    else:
        return HttpResponseRedirect('..')


def deletetodo(request, id):
    item_to_delete = TodoItem.objects.get(id=id)
    item_to_delete.delete()
    return HttpResponseRedirect('/')
